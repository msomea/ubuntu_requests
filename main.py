import requests
import os
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import hashlib

def fetch_images_from_page(page_url):
    """Scrape a webpage for images and download them."""
    try:
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the webpage
        response = requests.get(page_url, timeout=10)
        response.raise_for_status()

        # Parse the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all("img")
        if not img_tags:
            print(f"✗ No images found on: {page_url}")
            return

        for img in img_tags:
            img_src = img.get("src")
            if not img_src:
                continue

            # Resolve relative URLs
            img_url = urljoin(page_url, img_src)

            try:
                # Download the image
                img_resp = requests.get(img_url, timeout=10, stream=True)
                img_resp.raise_for_status()

                # Validate Content-Type
                content_type = img_resp.headers.get("Content-Type", "")
                if not content_type.startswith("image/"):
                    print(f"✗ Skipping non-image: {img_url}")
                    continue

                # Extract filename
                parsed_url = urlparse(img_url)
                filename = os.path.basename(parsed_url.path)
                if not filename:
                    filename = "image.jpg"

                # Add hash to avoid duplicates
                img_data = img_resp.content
                file_hash = hashlib.md5(img_data).hexdigest()
                name, ext = os.path.splitext(filename)
                filename = f"{name}_{file_hash[:8]}{ext}"
                filepath = os.path.join("Fetched_Images", filename)

                if not os.path.exists(filepath):
                    with open(filepath, "wb") as f:
                        f.write(img_data)
                    print(f"✓ Downloaded: {filename}")
                else:
                    print(f"⚠ Skipped duplicate: {filename}")

            except requests.exceptions.RequestException as e:
                print(f"✗ Failed to download image: {img_url} ({e})")

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to fetch webpage: {page_url} ({e})")
    except Exception as e:
        print(f"✗ Error processing {page_url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Scraper")
    print("A tool for mindfully collecting images from webpages\n")

    urls = input("Enter webpage URLs separated by commas: ").split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_images_from_page(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
