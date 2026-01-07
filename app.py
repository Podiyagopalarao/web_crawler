from flask import Flask, render_template, request, jsonify, send_file
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
        
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = soup.title.text if soup.title else "No Title"
        
        links = []
        for link in soup.find_all("a"):
            href = link.get("href")
            text = link.text.strip() or "No Text"
            if href:
                full_url = urljoin(url, href)
                links.append({'text': text, 'url': full_url})
        
        # Limit to first 100 links for performance in UI
        return jsonify({
            'title': title,
            'url': url,
            'links': links[:500], 
            'total_count': len(links)
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download_csv', methods=['POST'])
def download_csv():
    data = request.json
    links = data.get('links', [])
    source_url = data.get('url', '')
    page_title = data.get('title', '')
    
    # Create in-memory CSV
    proxy = io.StringIO()
    writer = csv.writer(proxy)
    writer.writerow(["Source URL", "Page Title", "Link Text", "Link URL"])
    
    for link in links:
        writer.writerow([source_url, page_title, link.get('text'), link.get('url')])
        
    # Convert to bytes for download
    mem = io.BytesIO()
    mem.write(proxy.getvalue().encode('utf-8'))
    mem.seek(0)
    
    return send_file(
        mem,
        mimetype='text/csv',
        as_attachment=True,
        download_name='crawled_data.csv'
    )

if __name__ == '__main__':
    app.run(debug=True)
