import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# Take website input
url = input("Enter website URL: ")

# Open website
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get title
title = soup.title.text if soup.title else "No Title"

# Open CSV file
with open("extracted_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Website URL", "Page Title", "Link"])

    # Extract links
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            full_url = urljoin(url, href)
            writer.writerow([url, title, full_url])

print("\nData saved successfully in extracted_data.csv")
