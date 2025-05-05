import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from zipfile import ZipFile
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: python download_pdfs.py <BASE_URL>")
        sys.exit(1)

    base_url = sys.argv[1]

    # Create download directory
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)

    # Generate ZIP filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"download_{timestamp}.zip"

    # Fetch the webpage
    print(f"Fetching: {base_url}")
    response = requests.get(base_url)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all PDF links
    pdf_links = []
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href.lower().endswith(".pdf"):
            full_url = urljoin(base_url, href)
            pdf_links.append(full_url)

    print(f"Found {len(pdf_links)} PDF files.")

    # Download all PDFs
    downloaded_files = []
    for url in pdf_links:
        filename = url.split("/")[-1]
        filepath = os.path.join(download_dir, filename)
        if not os.path.exists(filepath):
            print(f"Downloading {filename}...")
            pdf_response = requests.get(url)
            with open(filepath, "wb") as f:
                f.write(pdf_response.content)
        downloaded_files.append(filepath)

    # Create ZIP archive
    print(f"Creating ZIP archive: {zip_filename}")
    with ZipFile(zip_filename, 'w') as zipf:
        for file_path in downloaded_files:
            zipf.write(file_path, os.path.basename(file_path))

    print("✅ Done!")

if __name__ == "__main__":
    main()
