import requests
import os
from urllib.parse import urlparse
import hashlib

def fetch_image(url):
    """Fetch and save an image from a given URL."""
    try:
        # Create directory if it doesn't exist
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image with a timeout for safety
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Handle HTTP errors

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If URL has no file name
            filename = "downloaded_image.jpg"

        # Prevent duplicates using a hash of the content
        file_hash = hashlib.md5(response.content).hexdigest()
        name, ext = os.path.splitext(filename)
        filename = f"{name}_{file_hash[:8]}{ext}"  # Add hash to filename

        filepath = os.path.join("Fetched_Images", filename)

        # Save only if not already present
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
        else:
            print(f"⚠ Skipped duplicate: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Enter image URLs separated by commas: ").split(",")

    for url in urls:
        url = url.strip()
        if url:
            fetch_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
