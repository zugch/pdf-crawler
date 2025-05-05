# 📂 PDF Downloader from Web Archive Pages

A generic Python script to download all PDF files from a given web page and package them into a timestamped ZIP archive.

## 🚀 Features

* Takes a base URL as a command-line argument
* Scans the page for all `.pdf` links (absolute or relative)
* Downloads all found PDF files into a `downloads/` directory
* Creates a ZIP archive named like `download_YYYYMMDD_HHMMSS.zip`
* Compatible with GitHub Codespaces and local environments

---

## 💻 Usage

### GitHub Codespaces (Recommended)

1. Open this repository in a Codespace:

   * Click **Code → Codespaces → Create codespace**

2. Run the script in the terminal with a base URL:

```bash
python download_pdfs.py <BASE_URL>
```

#### Example:

```bash
python download_pdfs.py https://allschwilerwochenblatt.ch/zeitungsarchiv/index.html
```

### Locally

1. Make sure you have Python 3.7 or later.
2. Install the dependencies:

```bash
pip install requests beautifulsoup4
```

3. Run the script with a URL:

```bash
python download_pdfs.py <BASE_URL>
```

---

## 🗃️ Output

* All PDFs are downloaded into the `downloads/` folder.
* A ZIP archive is created in the root directory, named:

```
download_YYYYMMDD_HHMMSS.zip
```

Example:

```
download_20250505_144512.zip
```

---

## 📁 Project Structure

```
.
├── .devcontainer/           # Dev container config for Codespaces
│   └── devcontainer.json
├── downloads/               # Folder for downloaded PDFs
├── download_pdfs.py         # Main script
├── README.md                # This file
└── .gitignore               # Excludes downloads and ZIPs from Git
```

---

## 📝 License

MIT License – free to use, modify, and share with attribution.

---

## 🤝 Contributions

Suggestions, improvements, or bug fixes are welcome!
Feel free to open an issue or submit a pull request.
