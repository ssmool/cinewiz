from rembg import remove
from PIL import Image, ImageDraw, ImageFont
import requests
from bs4 import BeautifulSoup
import os
import uuid
import io
import time
import re
from urllib.parse import quote

# ==================== CONFIGURATION ====================
_app_path = os.getcwd()
_output_dir = f'{_app_path}/_out'
_fonts_dir = f'{_app_path}/_lib/_fonts'
os.makedirs(_output_dir, exist_ok=True)
os.makedirs(_fonts_dir, exist_ok=True)

# Create a default font file if needed
_default_font_path = None
for font_path in [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "C:\\Windows\\Fonts\\Arial.ttf",
    f'{_fonts_dir}/Montserrat-Regular.ttf'
]:
    if os.path.exists(font_path):
        _default_font_path = font_path
        break

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
        position=(0,0)
        try:
            img = Image.open(image_path)
            
            # Remove background if requested (skip for background images)
            if remove_bg and 'background' not in image_path.lower():
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
    
    def add_text(self, text, position=(10, 10), font_size=20, color=(0, 0, 0), font_path=None, multiline=False):
        """Add text to the composition with optional multiline support"""
        draw = ImageDraw.Draw(self.canvas)
        
        # Split text into lines for multiline
        if multiline and '\n' not in text:
            # Auto-wrap text at 50 characters
            words = text.split()
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                if current_length + len(word) + 1 <= 50:
                    current_line.append(word)
                    current_length += len(word) + 1
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
                    current_length = len(word)
            if current_line:
                lines.append(' '.join(current_line))
            text = '\n'.join(lines)
        
        try:
            # Try to use specified font or default
            if font_path and os.path.exists(font_path):
                font = ImageFont.truetype(font_path, font_size)
            elif _default_font_path:
                font = ImageFont.truetype(_default_font_path, font_size)
            else:
                font = ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        
        if multiline:
            draw.multiline_text(position, text, fill=color, font=font)
        else:
            draw.text(position, text, fill=color, font=font)
    
    def save_composition(self, filename="composition.png"):
        """Save the final composition"""
        output_path = f'{_output_dir}/{filename}'
        self.canvas.save(output_path, 'PNG')
        print(f"Composition saved: {output_path}")
        return output_path

# ==================== BING IMAGE SCRAPER ====================
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
            
            # Clean and deduplicate URLs
            clean_urls = []
            for url in image_urls:
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
            
            # Determine file extension from content-type
            content_type = response.headers.get('content-type', '')
            if 'jpeg' in content_type or 'jpg' in content_type:
                ext = '.jpg'
            elif 'png' in content_type:
                ext = '.png'
            elif 'gif' in content_type:
                ext = '.gif'
            else:
                ext = '.jpg'
            
            filename = f"{keyword}_{uuid.uuid4().hex[:8]}{ext}"
            filepath = f'{_output_dir}/{filename}'
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            return filepath
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None

# ==================== PARSE PROMPT FUNCTION ====================
def parse_prompt(search_query):
    """
    Parse the prompt to separate text in quotes (which won't be searched)
    from image keywords (which will be searched)
    """
    image_keywords = []
    text_entries = []
    
    i = 0
    length = len(search_query)
    
    while i < length:
        if search_query[i] == '"':
            # Found opening quote
            i += 1
            start = i
            # Find closing quote
            while i < length and search_query[i] != '"':
                i += 1
            text_content = search_query[start:i]
            if text_content:
                text_entries.append(text_content)
            i += 1
        elif search_query[i].strip():  # Non-space character
            # Extract keyword
            start = i
            while i < length and search_query[i] != ' ':
                i += 1
            keyword = search_query[start:i].strip()
            if keyword and keyword != '"':
                image_keywords.append(keyword)
        else:
            i += 1
    
    return image_keywords, text_entries

# ==================== MAIN FUNCTION ====================
def main():
    print("=" * 60)
    print("CINEWIZ GENAI - Generate Images from Prompt")
    print("=" * 60)
    print("\nInstructions:")
    print("- Enter words without quotes to search and download images")
    print("- Enter text inside \"quotes\" to add as text overlay (not searched)")
    print("- Example: cat dog \"Hello World\" bird")
    print("=" * 60)
    
    # Get search query from user
    search_query = input("\nEnter prompt: ").strip()
    if not search_query:
        print("Error: No prompt entered!")
        return
    
    # Parse the prompt to separate image keywords and text
    image_keywords, text_entries = parse_prompt(search_query)
    
    print(f"\n📷 Image keywords to search: {image_keywords if image_keywords else 'None'}")
    print(f"📝 Text overlays to add: {text_entries if text_entries else 'None'}")
    
    if not image_keywords:
        print("\nWarning: No image keywords found! Only text will be added.")
    
    # Initialize components
    scraper = BingImageScraper()
    composer = ImageComposer(width=1920, height=1080)
    composer.create_canvas(color=(240, 240, 240))
    
    # Layout positions for images (grid of 3x3)
    positions = [
        (50, 100), (690, 100), (1330, 100),
        (50, 460), (690, 460), (1330, 460),
        (50, 820), (690, 820), (1330, 820)
    ]
    image_size = (580, 320)
    
    downloaded_images = []
    
    # Search and download images for each keyword
    for idx, keyword in enumerate(image_keywords[:9]):  # Max 9 images
        print(f"\n🔍 Searching for: {keyword}")
        
        image_urls = scraper.search_images(keyword, limit=2)
        
        if not image_urls:
            print(f"❌ No images found for '{keyword}'")
            continue
        
        # Try to download an image
        image_path = None
        for url in image_urls:
            print(f"📥 Attempting to download: {url[:60]}...")
            image_path = scraper.download_image(url, keyword)
            if image_path:
                break
        
        if image_path:
            downloaded_images.append({
                'path': image_path,
                'keyword': keyword,
                'remove_bg': True
            })
            print(f"✅ Downloaded: {os.path.basename(image_path)}")
        else:
            print(f"❌ Failed to download image for '{keyword}'")
        
        time.sleep(0.5)  # Small delay to avoid rate limiting
    
    # Add title text
    title = "CINEWIZ IMAGE COMPOSITION"
    composer.add_text(
        title,
        position=(composer.width // 2 - 200, 20),
        font_size=36,
        color=(0, 0, 0)
    )
    
    # Add subtitle with search info
    if image_keywords:
        subtitle = f"Images: {' | '.join(image_keywords[:5])}"
        composer.add_text(
            subtitle,
            position=(50, 65),
            font_size=18,
            color=(100, 100, 100)
        )
    
    # Add all images to composition
    print("\n🎨 Composing Images...")
    for i, img_info in enumerate(downloaded_images):
        if i >= len(positions):
            break
            
        pos = positions[i]
        print(f"  Adding image {i+1}: {img_info['keyword']} at position {pos}")
        
        # Add image with background removal
        composer.add_image(
            img_info['path'], 
            position=pos, 
            size=image_size,
            remove_bg=img_info['remove_bg']
        )
        
        # Add label for the keyword below the image
        label_pos = (pos[0] + 10, pos[1] + image_size[1] + 5)
        composer.add_text(
            f"📷 {img_info['keyword']}",
            position=label_pos,
            font_size=16,
            color=(80, 80, 80)
        )
    
    # Add text overlays from quotes
    print("\n📝 Adding text overlays...")
    text_y_position = 100 if downloaded_images else 100
    text_x_position = 50
    
    for i, text_content in enumerate(text_entries):
        print(f"  Adding text: '{text_content}'")
        
        # Calculate position for each text (stack vertically if multiple)
        y_offset = text_y_position + (i * 80)
        
        # Add decorative background for text
        composer.add_text(
            f"「 {text_content} 」",
            position=(text_x_position + 5, y_offset + 5),
            font_size=48,
            color=(200, 200, 200),
            multiline=False
        )
        
        # Add main text
        composer.add_text(
            f"「 {text_content} 」",
            position=(text_x_position, y_offset),
            font_size=48,
            color=(50, 50, 150),
            multiline=False
        )
    
    # Add footer with timestamp and info
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    footer_text = f"Generated by CINEWIZ | {timestamp} | Images: {len(downloaded_images)} | Texts: {len(text_entries)}"
    composer.add_text(
        footer_text,
        position=(50, composer.height - 40),
        font_size=14,
        color=(150, 150, 150)
    )
    
    # Save the final composition
    output_filename = f"cinewiz_composition_{uuid.uuid4().hex[:8]}.png"
    output_path = composer.save_composition(output_filename)
    
    # Try to display the image
    try:
        composer.canvas.show()
        print("\n🖼️ Image displayed on screen.")
    except Exception as e:
        print(f"\n⚠️ Could not display image automatically: {e}")
    
    # Cleanup
    print("\n🧹 Cleanup:")
    keep_images = input("Keep downloaded images? (y/n): ").strip().lower()
    
    if keep_images != 'y':
        for img_info in downloaded_images:
            try:
                if os.path.exists(img_info['path']):
                    os.remove(img_info['path'])
                    print(f"  Removed: {os.path.basename(img_info['path'])}")
            except Exception as e:
                print(f"  Could not remove {img_info['path']}: {e}")
    else:
        print(f"  Downloaded images saved in: {_output_dir}")
    
    print(f"\n✅ Process completed successfully!")
    print(f"📁 Final composition saved at: {output_path}")

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
        from PIL import Image, ImageDraw, ImageFont
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
