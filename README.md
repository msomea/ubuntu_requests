# Ubuntu Image Fetcher

A mindful Python tool for fetching and organizing images from the web.  
This script downloads images from user-provided URLs, validates them, prevents duplicates, and saves them in an organized directory.

## Features

- **Multiple URL support** – Enter several image URLs at once (comma-separated).
- **Content-Type validation** – Ensures only images are downloaded.
- **Automatic directory creation** – Saves all images into a `Fetched_Images` folder.
- **Duplicate prevention** – Uses MD5 hashing to avoid saving the same image twice.
- **Graceful error handling** – Prevents crashes when connections fail.

## Requirements

- Python 3.x
- `requests` library

Install dependencies using:
```bash
pip install requests


Usage

1. Clone or download this repository.

2. Run the script:

python main.py

3. Enter one or multiple URLs containing images separated by commas when prompted.

Example:

Please enter the image URLs: https://example.com/image1.jpg, https://example.com/image2.png


4. Images will be saved in the Fetched_Images folder.

Precautions

Only files with Content-Type starting with image/ will be downloaded.

Duplicates are detected and skipped using content hashing.

Ensure you have permission to download and store the images.

Ubuntu Principles

This project embodies Ubuntu principles:

Community: Connects to the wider web community by fetching and sharing resources.

Respect: Handles errors gracefully without crashing.

Sharing: Organizes images for easy access and redistribution.

Practicality: A lightweight tool for real-world use.

License

This project is open-source under the MIT License.
