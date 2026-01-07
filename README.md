# Web Crawler Pro

A simple yet powerful web crawler built with Python and Flask. This tool allows you to crawl websites to extract page titles and all outgoing links, with options to view the data in a web interface or download it as a CSV file.

## Features

- **Web Interface:** User-friendly web GUI to input URLs and view results.
- **Link Extraction:** Extracts all links (hrefs) and their link text from the target URL.
- **CSV Export:** Download the crawled data (Source URL, Page Title, Link Text, Link URL) as a CSV file.
- **CLI Mode:** Includes a standalone command-line script (`crawler.py`) for quick terminal-based crawling.

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone or download this repository.
2. Open the project folder.

## Usage

### Method 1: Web Interface (Recommended)

1. Double-click the `run.bat` file. 
   - This script automatically installs the required dependencies (`flask`, `requests`, `beautifulsoup4`) and starts the web server.
2. Your default web browser should open automatically to `http://127.0.0.1:5000`.
3. Enter a URL (e.g., `example.com`) and click **Crawl**.
4. View the results or click **Download CSV** to save them.

### Method 2: Manual Setup (Command Line)

1. Open a terminal/command prompt in the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

### Method 3: CLI Script

If you prefer a command-line interface without the web server:

1. Run the crawler script:
   ```bash
   python crawler.py
   ```
2. Enter the URL when prompted.
3. The results will be saved to `extracted_data.csv` in the same directory.

## Project Structure

- `app.py`: Main Flask application.
- `crawler.py`: Standalone CLI crawler script.
- `run.bat`: Windows batch script for easy setup and launch.
- `templates/index.html`: HTML template for the web interface.
- `static/style.css`: CSS styling.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for the GUI.
- **BeautifulSoup4**: HTML parsing and data extraction.
- **Requests**: HTTP library for fetching web pages.
