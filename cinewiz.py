#pip install Pillow qrcode

import uuid
import os
from PIL import Image, ImageDraw, ImageFont, ImageChops
# Note: Pillow does not use 'PX' for font size; it uses 'pt' (points). 
# The script uses points for consistency.
import qrcode 

# --- Global Variables ---
LST_IMAGES = []
LST_CAPTION = []
CINEWIZ_GRAYVISION = None  # The final Pillow Image object
GLOBAL_SUBJECT = ""

# A4 dimensions in pixels (Portrait @ 150 DPI for a manageable size)
A4_WIDTH = 1240
A4_HEIGHT = 1754
BOTTOM_SPACE_HEIGHT = 240
STAGE_HEIGHT = A4_HEIGHT
STAGE_WIDTH = A4_WIDTH

# --- Utility: Mock Image Creator ---
def _create_mock_image(path="mock_image.png"):
    """Creates a simple placeholder image for the script to use."""
    if not os.path.exists(path):
        img = Image.new('RGB', (800, 600), color='blue')
        d = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()
        d.text((10, 10), "MOCK IMAGE PLACEHOLDER", fill=(255, 255, 255), font=font)
        img.save(path)
        print(f"Created mock image file: {path}")
    return path

# --- Core Functions ---

def _start_global_variables(orientation="PORTRAIT"):
    """
    INITIAL: Initializes global variables, LST_IMAGES, LST_CAPTION,
    and defines the stage (A4 Portrait or Landscape).
    """
    global LST_IMAGES, LST_CAPTION, STAGE_WIDTH, STAGE_HEIGHT, CINEWIZ_GRAYVISION

    print(f"\n--- 1. INITIAL: GLOBAL VARIABLES SETUP (Orientation: {orientation}) ---")

    # DEF _START GLOBAL VARIABLES
    LST_IMAGES = [{
        "INDEX": 0,
        "PATH": "background_image.jpg",
        "FILE_NAME": "background",
        "DESCRIPTION": "The main background layer",
        "KEYWORDS": "",
        "FILTERS": "",
        "POSITION-FRONT": 0,
        "POSITION_X": 0,
        "POSITION_Y": 0
    }]

    LST_CAPTION = [{
        "GUID": str(uuid.uuid4()),
        "TEXT": "CINEWIZ AI Generated Content",
        "KEYWORDS": "AI, Generative",
        "POSITION-FRONT": 0,
        "POSITION_X": 50,
        "POSITION_Y": 50,
        "FONT-SIZE": 36, # Using a reasonable point size (not 14PX)
        "FONT-FAMILY": "Default"
    }]

    # Define A4 stage dimensions (Landscape or Portrait)
    if orientation.upper() == "LANDSCAPE":
        STAGE_WIDTH = A4_HEIGHT
        STAGE_HEIGHT = A4_WIDTH
    else:  # PORTRAIT
        STAGE_WIDTH = A4_WIDTH
        STAGE_HEIGHT = A4_HEIGHT

    # Create the initial blank stage (Default RGB: white)
    CINEWIZ_GRAYVISION = Image.new("RGB", (STAGE_WIDTH, STAGE_HEIGHT), color="white")
    print(f"Stage created: {STAGE_WIDTH}x{STAGE_HEIGHT} (A4 {orientation})")


def _get_prompt(keyword: str):
    """
    GETS A KEYWORD, separates it by hashtags for GLOBAL_SUBJECT, 
    and simulates defining image search prompts (including <BACKGROUND>IMAGE</BACKGROUND>).
    """
    global GLOBAL_SUBJECT, LST_IMAGES

    print(f"\n--- 2. DEF _GET_PROMPT for: '{keyword}' ---")

    # Separate keywords and create GLOBAL_SUBJECT
    subject_keywords = [k.strip() for k in keyword.split() if k.strip()]
    GLOBAL_SUBJECT = "#".join(subject_keywords)
    print(f"GLOBAL_SUBJECT set: {GLOBAL_SUBJECT}")

    # Define a background search tag
    background_search = f"<BACKGROUND>IMAGE</BACKGROUND> {keyword} artistic background"
    LST_IMAGES[0]["DESCRIPTION"] = background_search
    LST_IMAGES[0]["KEYWORDS"] = keyword

    # Define a subject image to search and set its position
    new_index = len(LST_IMAGES)
    LST_IMAGES.append({
        "INDEX": new_index,
        "PATH": "subject_image.png", # MOCK path
        "FILE_NAME": "subject_image",
        "DESCRIPTION": f"A vibrant 3D render of {keyword}",
        "KEYWORDS": keyword,
        "FILTERS": "Transparent Background, PNG",
        "POSITION-FRONT": 1,
        "POSITION_X": 200,
        "POSITION_Y": 300
    })

    print(f"LST_IMAGES updated with AI prompt and position data.")


def _download_images(image_data: dict) -> str:
    """
    Mocks/simulates downloading an image from URL (Flickr/Web), local path, or SVN.
    Returns the path to the file.
    """
    source = image_data.get("PATH", "")
    print(f"\n--- 3. DOWNLOAD IMAGE (Index: {image_data['INDEX']}) ---")

    if source.lower().startswith("http"):
        # MOCK: Web/Flickr download logic
        print(f"MOCK: Searching Flickr/Web for: {image_data['DESCRIPTION']}")
        # In a real system: requests.get(url) -> save file
        return "mock_image.png"

    elif source.lower().startswith("/cinewiz/svn/svn.cinemapz"):
        # MOCK: SVN Read
        print(f"MOCK: Reading SVN path: {source} for URLs.")
        # In a real system: SVN client or specific file I/O for URL list
        # We will assume a file is found and downloaded.
        return "mock_image.png"

    elif source:
        # Local path
        return _create_mock_image(source)
    
    return _create_mock_image() # Default mock


def _add_images(index: int):
    """
    Uses Pillow to define the stage and image to stage.
    """
    global CINEWIZ_GRAYVISION, LST_IMAGES, STAGE_WIDTH, STAGE_HEIGHT

    if index >= len(LST_IMAGES):
        print(f"ERROR: Image index {index} not found.")
        return

    image_data = LST_IMAGES[index]
    img_path = _download_images(image_data) # Mocks download and gets path

    try:
        # Open the image. Using RGB scale as requested (default)
        img = Image.open(img_path).convert("RGB")
        print(f"Adding image {index} (Size: {img.size})")
        
        target_height = STAGE_HEIGHT - BOTTOM_SPACE_HEIGHT
        
        if index == 0: # Background
            # Scale to cover the entire stage (excluding QR space)
            w_ratio = STAGE_WIDTH / img.width
            h_ratio = target_height / img.height
            ratio = max(w_ratio, h_ratio)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

            # Center crop
            left = (resized_img.width - STAGE_WIDTH) / 2
            top = (resized_img.height - target_height) / 2
            right = (resized_img.width + STAGE_WIDTH) / 2
            bottom = (resized_img.height + target_height) / 2
            resized_img = resized_img.crop((left, top, right, bottom))
            position = (0, 0)
        else: # Subject image
            # Resize subject image (e.g., to 40% of stage width)
            max_size = int(STAGE_WIDTH * 0.4)
            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
            resized_img = img
            position = (int(image_data["POSITION_X"]), int(image_data["POSITION_Y"]))

        # Paste the image
        # Use a temporary image for `mask` if needed (e.g., for PNG transparency), but
        # since we convert to RGB, we stick to simple paste for this example.
        CINEWIZ_GRAYVISION.paste(resized_img, position)

    except FileNotFoundError:
        print(f"ERROR: Image file not found at {img_path}. Skipping.")
    except Exception as e:
        print(f"ERROR processing image {index}: {e}")


def _add_text(index: int):
    """
    Adds text to the image using fields from LST_CAPTION.
    """
    global CINEWIZ_GRAYVISION, LST_CAPTION

    if index >= len(LST_CAPTION):
        print(f"ERROR: Caption index {index} not found.")
        return

    caption_data = LST_CAPTION[index]
    draw = ImageDraw.Draw(CINEWIZ_GRAYVISION)

    text_content = caption_data["TEXT"]
    x = int(caption_data["POSITION_X"])
    y = int(caption_data["POSITION_Y"])
    font_size = caption_data["FONT-SIZE"]

    try:
        # Attempt to load a common font
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()
        print(f"Warning: Using default font for caption {index}.")

    print(f"\n--- 4. DEF _ADD_TEXT: '{text_content}' at ({x}, {y}) ---")

    draw.text((x, y), text_content, font=font, fill=(0, 0, 0)) # Default fill is black


def _add_qrcode(keyword: str, url_to_image: str):
    """
    Creates the 240px bottom blank space, adds the QR code (200x200px) 
    and the descriptive text with 10px margins.
    """
    global CINEWIZ_GRAYVISION, STAGE_WIDTH, STAGE_HEIGHT, BOTTOM_SPACE_HEIGHT

    print(f"\n--- 5. DEF _ADD_QRCODE & FOOTER ({BOTTOM_SPACE_HEIGHT}px) ---")

    # 1. Create the bottom blank space (white rectangle)
    bottom_y_start = STAGE_HEIGHT - BOTTOM_SPACE_HEIGHT
    draw = ImageDraw.Draw(CINEWIZ_GRAYVISION)
    draw.rectangle([0, bottom_y_start, STAGE_WIDTH, STAGE_HEIGHT], fill="white")

    # 2. Generate the QR Code (200x200 px)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4, # Controls size, aiming for ~200px
        border=1,
    )
    qr.add_data(url_to_image)
    qr.make(fit=True)
    qr_img_pil = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    qr_size = (200, 200)
    qr_img_pil = qr_img_pil.resize(qr_size)

    # 3. Define positions with 10px margin (QR Code is right-aligned)
    margin = 10
    qr_x = STAGE_WIDTH - qr_size[0] - margin 
    qr_y = bottom_y_start + (BOTTOM_SPACE_HEIGHT - qr_size[1]) // 2 

    # 4. Paste QR Code
    CINEWIZ_GRAYVISION.paste(qr_img_pil, (qr_x, qr_y))

    # 5. Add text: "CINEWIZ AI FOR IMAGES GENAI"
    text_content = f"CINEWIZ AI FOR IMAGES GENAI (Subject: {keyword})"
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Text position: Left side, vertically centered
    text_x = margin
    text_bbox = draw.textbbox((0, 0), text_content, font=font)
    text_height = text_bbox[3] - text_bbox[1]
    text_y = bottom_y_start + (BOTTOM_SPACE_HEIGHT - text_height) // 2

    draw.text((text_x, text_y), text_content, font=font, fill=(0, 0, 0))


def _image_done():
    """
    Finalizes and saves the global CINEWIZ_GRAYVISION image.
    CINEWIZ_GRAYVISION=UUID.UUID4(USING A GUID NAME)_{GLOBAL_SUBJECT}.JPEG
    """
    global CINEWIZ_GRAYVISION, GLOBAL_SUBJECT

    print("\n--- 6. DEF _IMAGE_DONE: FINALIZING IMAGE ---")
    if CINEWIZ_GRAYVISION is None:
        print("ERROR: CINEWIZ_GRAYVISION is not initialized.")
        return

    # Generate the final file name
    guid_name = uuid.uuid4().hex
    safe_subject = GLOBAL_SUBJECT.replace('#', '_').replace(' ', '_').strip('_')
    final_file_name = f"/cinewiz-ai/download/CINEWIZ_GRAYVISION_{guid_name}_{safe_subject}.JPEG"

    try:
        CINEWIZ_GRAYVISION.save(final_file_name, "JPEG", quality=95)
        print(f"\nSUCCESS! Image saved as: {final_file_name}")
        return final_file_name
    except Exception as e:
        print(f"ERROR saving image: {e}")
        return None

# --- Demonstration Block ---
if __name__ == "__main__":
    
    # 0. Create the mock image file needed for the demo
    _create_mock_image()
    
    # 1. Initialize Global Variables and the A4 Stage
    _start_global_variables(orientation="PORTRAIT")

    # 2. Get Prompt and set up LST_IMAGES
    SUBJECT_KEYWORD = "Cyberpunk Samurai in Neon City"
    _get_prompt(SUBJECT_KEYWORD)

    # 3. Add Images (Background and Subject)
    # The image path is resolved/downloaded inside _add_images via _download_images
    for img_index in [0, 1]:
        _add_images(img_index)

    # 4. Add Text (The default caption)
    _add_text(0)

    # 5. Add QR Code and Footer
    MOCK_URL = "https://www.cinewiz.com/image/" + LST_CAPTION[0]["GUID"]
    _add_qrcode(SUBJECT_KEYWORD, MOCK_URL)

    # 6. Finalize and Save
    final_path = _image_done()
    
    if final_path:
        print(f"\nSuccessfully generated image: {final_path}")
