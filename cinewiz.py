from rembg import remove
from PIL import Image, ImageDraw, ImageFont
import requests
from bs4 import BeautifulSoup
import os
import uuid
import io
import time
import shutil
import re
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor

# ==================== CONFIGURATION ====================
_app_path = os.getcwd()
_output_dir = f'{_app_path}/_out'
os.makedirs(_output_dir, exist_ok=True)

# ==================== IMAGE COMPOSER CLASS ====================
class ImageComposer:
    def __init__(self, width=1920, height=1080):
        self.width = width
        self.height = height
        self.canvas = Image.new('RGBA', (width, height), (255, 255, 255, 255))
        self.temp_files = []
        
    def create_canvas(self, color=(255, 255, 255)):
        """Create a new canvas"""
        self.canvas = Image.new('RGBA', (self.width, self.height), (*color, 255))
        return self.canvas
    
    def add_image(self, image_path, position=(0, 0), size=None, remove_bg=False):
        """Add an image to the composition"""
        try:
            img = Image.open(image_path)
            
            # Remove background if requested
            try:
                if(image_path.index('background') < 1):
                  if remove_bg:
                      print(f"REMOVE BG({image_path}):")
                      img = self.remove_background(img)
            except:
                print(f"REMOVE BG({image_path}):")
                img = self.remove_background(img)
            
            # Resize if size specified
            if size:
                img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Convert to RGBA if needed
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Paste onto canvas
            self.canvas.paste(img, position, img if img.mode == 'RGBA' else None)
            return True
        except Exception as e:
            print(f"Error adding image {image_path}: {e}")
            return False
    
    def remove_background(self, image):
        """Remove background from image using rembg"""
        try:
            # Convert PIL to bytes
            img_bytes = io.BytesIO()
            image.save(img_bytes, format='PNG')
            img_bytes = img_bytes.getvalue()
            
            # Remove background
            output_bytes = remove(img_bytes)
            
            # Convert back to PIL
            result = Image.open(io.BytesIO(output_bytes))
            return result
        except Exception as e:
            print(f"Error removing background: {e}")
            return image
    
    def add_text(self, text, position=(10, 10), font_size=20, color=(0, 0, 0)):
        """Add text to the composition"""
        draw = ImageDraw.Draw(self.canvas)
        try:
            # Try to use a system font (Linux/Mac)
            font_paths = [
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                "/System/Library/Fonts/Helvetica.ttc",
                "C:\\Windows\\Fonts\\Arial.ttf"
            ]
            font = None
            for font_path in font_paths:
                if os.path.exists(font_path):
                    font = ImageFont.truetype(font_path, font_size)
                    break
            if font is None:
                font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        
        draw.text(position, text, fill=color, font=font)
    
    def save_composition(self, filename="composition.png"):
        """Save the final composition"""
        output_path = f'{_output_dir}/{filename}'
        self.canvas.save(output_path, 'PNG')
        print(f"Composition saved: {output_path}")
        return output_path

# ==================== BING IMAGE SCRAPER (No imghdr dependency) ====================
class BingImageScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
    
    def search_images(self, keyword, limit=5):
        """Search for images using Bing"""
        search_url = f"https://www.bing.com/images/search?q={quote(keyword)}&form=HDRSC2&first=1"
        
        try:
            response = requests.get(search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Extract image URLs using multiple methods
            image_urls = []
            
            # Method 1: Extract from murl parameter in JavaScript
            murl_matches = re.findall(r'murl&quot;:&quot;([^&]+)&quot;', response.text)
            image_urls.extend(murl_matches)
            
            # Method 2: Extract from imgurl parameter
            imgurl_matches = re.findall(r'imgurl:&quot;([^&]+)&quot;', response.text)
            image_urls.extend(imgurl_matches)
            
            # Method 3: Extract from data-src attributes
            soup = BeautifulSoup(response.text, 'html.parser')
            for img in soup.find_all('img', {'class': 'mimg'}):
                src = img.get('src') or img.get('data-src')
                if src and src.startswith('http'):
                    image_urls.append(src)
            
            # Method 4: Extract from thumbnail URLs
            thumb_matches = re.findall(r'turl&quot;:&quot;([^&]+)&quot;', response.text)
            image_urls.extend(thumb_matches)
            
            # Clean and deduplicate URLs
            clean_urls = []
            for url in image_urls:
                # Clean up escaped characters
                url = url.replace('\\u002f', '/').replace('\\/', '/')
                if url.startswith('http') and 'bing.com' not in url:
                    clean_urls.append(url)
            
            # Remove duplicates while preserving order
            unique_urls = []
            for url in clean_urls:
                if url not in unique_urls:
                    unique_urls.append(url)
            
            return unique_urls[:limit]
            
        except Exception as e:
            print(f"Error searching Bing for '{keyword}': {e}")
            return []
    
    def download_image(self, url, keyword):
        """Download image from URL"""
        try:
            response = requests.get(url, timeout=10, headers=self.headers)
            response.raise_for_status()
            
            # Determine file extension from content-type or URL
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            else:
                ext = '.jpg'  # Default to jpg
            
            filename = f"{keyword}_{uuid.uuid4().hex[:8]}{ext}"
            filepath = f'{_output_dir}/{filename}'
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            return filepath
        except Exception as e:
            print(f"Error downloading image from {url}: {e}")
            return None

# ==================== MAIN FUNCTION ====================
def main():
    print("=" * 60)
    print("Bing Image Search and Composition Tool (No API Key Required)")
    print("=" * 60)
    
    # Get search query from user
    search_query = input("\nEnter search terms (separate by spaces): ").strip()
    if not search_query:
        print("Error: No search terms entered!")
        return
    
    # Split into individual words
    keywords = search_query.split()
    print(f"\nSearching for: {', '.join(keywords)}")
    
    # Initialize components
    scraper = BingImageScraper()
    composer = ImageComposer(width=1920, height=1080)
    composer.create_canvas(color=(255, 255, 255))
    
    # Layout positions for images (grid of 3x3)
    positions = [
        (0, 0), (640, 0), (1280, 0),
        (0, 360), (640, 360), (1280, 360),
        (0, 720), (640, 720), (1280, 720)
    ]
    image_size = (600, 600)
    
    downloaded_images = []
    
    # Search and download ONE image for each keyword
    for idx, keyword in enumerate(keywords[:9]):  # Max 9 images for 3x3 grid
        print(f"\n--- Searching for: {keyword} ---")
        
        # Search for images
        image_urls = scraper.search_images(keyword, limit=3)
        
        if not image_urls:
            print(f"No images found for '{keyword}'")
            continue
        
        # Try to download an image
        image_path = None
        for url in image_urls:
            print(f"Attempting to download: {url[:80]}...")
            image_path = scraper.download_image(url, keyword)
            if image_path:
                break
        
        if image_path:
            downloaded_images.append({
                'path': image_path,
                'keyword': keyword,
                'remove_bg': True
            })
            print(f"✓ Downloaded: {os.path.basename(image_path)}")
        else:
            print(f"✗ Failed to download image for '{keyword}'")
        
        # Small delay to avoid rate limiting
        time.sleep(1)
    
    # Check if we have any images
    if not downloaded_images:
        print("\nNo images were downloaded. Please check your internet connection.")
        return
    
    # Add title text to composition
    composer.add_text(
        f"Bing Search Results: {search_query}", 
        position=(50, 50), 
        font_size=40, 
        color=(0, 0, 0)
    )
    
    # Add all images to composition
    print("\n--- Composing Images ---")
    for i, img_info in enumerate(downloaded_images):
        if i >= len(positions):
            break
            
        pos = positions[0]
        print(f"Adding image {i+1}: {img_info['keyword']} at position {pos}")
        
        # Add image with background removal
        composer.add_image(
            img_info['path'], 
            position=pos, 
            size=image_size,
            remove_bg=img_info['remove_bg']
        )
        
        # Add label for the keyword
        label_pos = (pos[0] + 10, pos[1] + image_size[1] + 10)
        composer.add_text(
            img_info['keyword'], 
            position=label_pos, 
            font_size=24, 
            color=(100, 100, 100)
        )
    
    # Add footer with timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    composer.add_text(
        f"Generated with Bing Image Search on: {timestamp}", 
        position=(50, composer.height - 50), 
        font_size=16, 
        color=(150, 150, 150)
    )
    
    # Save the final composition
    output_filename = f"bing_composition_{uuid.uuid4().hex[:8]}.png"
    output_path = composer.save_composition(output_filename)
    
    # Try to display the image
    try:
        composer.canvas.show()
        print("Image displayed on screen.")
    except Exception as e:
        print(f"Could not display image automatically: {e}")
    
    # Cleanup
    print("\n--- Cleanup ---")
    keep_images = input("Keep downloaded images? (y/n): ").strip().lower()
    
    if keep_images != 'y':
        for img_info in downloaded_images:
            try:
                if os.path.exists(img_info['path']):
                    os.remove(img_info['path'])
                    print(f"Removed: {os.path.basename(img_info['path'])}")
            except Exception as e:
                print(f"Could not remove {img_info['path']}: {e}")
    else:
        print(f"Downloaded images saved in: {_output_dir}")
    
    print(f"\n✓ Process completed successfully!")
    print(f"Final composition saved at: {output_path}")

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    # Check if required libraries are installed
    missing_libs = []
    
    try:
        from rembg import remove
        print("✓ rembg found")
    except ImportError:
        missing_libs.append("rembg")
    
    try:
        from PIL import Image
        print("✓ Pillow found")
    except ImportError:
        missing_libs.append("pillow")
    
    try:
        import requests
        print("✓ requests found")
    except ImportError:
        missing_libs.append("requests")
    
    try:
        from bs4 import BeautifulSoup
        print("✓ beautifulsoup4 found")
    except ImportError:
        missing_libs.append("beautifulsoup4")
    
    if missing_libs:
        print(f"\n✗ Missing required libraries: {', '.join(missing_libs)}")
        print(f"Please install them using: pip install {' '.join(missing_libs)}")
        exit(1)
    
    main()
