# 🗂️ PDF Downloader from Web Archive Pages

A generic Python script to download all PDF files from a given web page and package them into a timestamped ZIP archive.

## 🚀 Features

- Takes a base URL as a command-line argument
- Scans the page for all `.pdf` links (absolute or relative)
- Downloads all found PDF files into a `downloads/` directory
- Creates a ZIP archive named like `download_YYYYMMDD_HHMMSS.zip`
- Compatible with GitHub Codespaces and local environments

---

## 💻 Usage

### GitHub Codespaces (Recommended)

1. Open this repository in a Codespace:
   - Click **Code → Codespaces → Create codespace**

2. Run the script in the terminal with a base URL:

```bash
python download_pdfs.py <BASE_URL>
