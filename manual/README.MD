
## 🎬 Cinewiz - Theatre Movie RAG GEN-AI

![Python CiNEWIZ_RAG_GENAI Logo](../assets/cinewiz_cover.gif)

**Version:** 1.0 Beta

**Status:** Under Development  

**Author:** #asytrick

**Website:** [github.com/cinewiz](https://github.com/ssmool/cinewiz)  

**Contact:** eusmool@gmail.com  

**Cinewiz** is an open-source Python package designed to streamline the development of **multimodal applications** powered by **LLMs**, **RAG (Retrieval-Augmented Generation)**, and **web crawling**. It’s built for workflows that require dynamic content generation and automation in creative environments.

Use Cinewiz to:
- Generate **images from keywords** and visual prompts  
- Compose contextual **text content** using online data  
- Insert **QR codes** into generated artwork  
- Manage persistent URI lists for input/output resources  
- Expand and **globalize prompts** across multiple languages  
- Integrate easily with generative pipelines and AI toolkits

## CINEWIZOS TECHNICAL DEFINITIONS:

# 🎬 Cinewiz — AI Cinematic Image Generator (Python + Pillow)

**Cinewiz** is a Python-based library for generating cinematic, composited AI-style images using **Pillow** and **QRCode**.  
It allows developers to define layered visual scenes — including background, subjects, captions, and QR-tagged metadata — all in an automated workflow.

---

## 🚀 Features

- 🧱 **Layered image composition** (background, subjects, captions, QR footer)  
- 🧠 **Prompt-based scene definition** for concept generation  
- 🖼️ **A4-format layout engine** (portrait or landscape)  
- 🔤 **Text overlay support** with custom fonts and positioning  
- 📱 **QR code embedding** with dynamic metadata links  
- 🧩 **Mock image creation** for demo or offline mode  

---

## ⚙️ Installation

Install dependencies:

```bash
pip install Pillow qrcode
```

Then clone the repository:

```bash
git clone https://github.com/ssmool/cinewiz.git
cd cinewiz
```

Run the example:

```bash
python cinewiz.py
```

---

## 📁 Project Structure

```
cinewiz/
│
├── cinewiz.py          # Main script and API
├── output/             # (Optional) Generated images
└── README.md           # Documentation
```

---

## 💡 Quick Start Example

```python
from cinewiz import (
    _create_mock_image,
    _start_global_variables,
    _get_prompt,
    _add_images,
    _add_text,
    _add_qrcode,
    _image_done,
    LST_CAPTION
)

# 1. Create mock image
_create_mock_image()

# 2. Initialize global stage (A4 portrait)
_start_global_variables("PORTRAIT")

# 3. Define subject
keyword = "Cyberpunk Samurai in Neon City"
_get_prompt(keyword)

# 4. Add background and subject layers
for i in [0, 1]:
    _add_images(i)

# 5. Add caption text
_add_text(0)

# 6. Add QR code and footer
mock_url = "https://www.cinewiz.com/image/" + LST_CAPTION[0]["GUID"]
_add_qrcode(keyword, mock_url)

# 7. Finalize and save
final_path = _image_done()
print("Image generated at:", final_path)
```

---

## 🧩 Function Overview

| Function | Purpose |
|-----------|----------|
| `_create_mock_image()` | Creates a local placeholder image for demos |
| `_start_global_variables(orientation)` | Initializes global lists and A4 canvas (portrait/landscape) |
| `_get_prompt(keyword)` | Defines subject metadata and image prompts |
| `_download_images(image_data)` | Simulates image fetching from web, SVN, or local |
| `_add_images(index)` | Draws images (background/subject) onto the stage |
| `_add_text(index)` | Renders text captions with Pillow |
| `_add_qrcode(keyword, url)` | Adds QR metadata footer and label |
| `_image_done()` | Finalizes and saves the composed image to disk |

---

## 🧠 Technical Architecture

### 🏗️ Core Engine
Cinewiz centers around a **global stage** (`CINEWIZ_GRAYVISION`) which represents an A4 image surface (default **1240x1754 px** at 150 DPI).  
All elements — images, captions, and QR codes — are layered onto this stage.

### 📦 Data Structures

- `LST_IMAGES`: Holds metadata and composition info for each image layer  
  Example:
  ```python
  {
      "INDEX": 0,
      "PATH": "background_image.jpg",
      "DESCRIPTION": "The main background layer",
      "POSITION_X": 0,
      "POSITION_Y": 0
  }
  ```

- `LST_CAPTION`: Holds metadata for textual captions  
  Example:
  ```python
  {
      "GUID": "...",
      "TEXT": "CINEWIZ AI Generated Content",
      "POSITION_X": 50,
      "POSITION_Y": 50
  }
  ```

### 🎨 Rendering Workflow

1. **Initialize stage** with `_start_global_variables()`  
2. **Set prompts** via `_get_prompt()`  
3. **Add images** with `_add_images()` (background + subject)  
4. **Overlay text** via `_add_text()`  
5. **Embed QR footer** with `_add_qrcode()`  
6. **Finalize & save** via `_image_done()`

All rendering uses **Pillow**, and each step can be extended for real AI image fetching.

---

## 🧪 Example Output

By default, running `cinewiz.py` will:

1. Create a **mock image placeholder**
2. Generate a **white A4 portrait canvas**
3. Add **two layers** (background + subject)
4. Add a **caption** at (50, 50)
5. Embed a **QR footer** (with “CINEWIZ AI FOR IMAGES GENAI” text)
6. Save output as:

```
/cinewiz-ai/download/CINEWIZ_GRAYVISION_<GUID>_<subject>.JPEG
```

---

## 🔧 Extending Cinewiz

You can extend the library by:

- Replacing `_download_images()` with actual API calls (e.g., Flickr, Unsplash, Stable Diffusion)
- Adding custom effects to `_add_images()`
- Integrating new font and filter logic for stylized captions
- Changing stage dimensions for print-quality exports (300 DPI)

---

## 🧑‍💻 Contributing

Contributions are welcome!  
If you have ideas for integrating AI image models or extending functionality:

1. Fork this repo  
2. Create a new branch (`feature/your-feature`)  
3. Commit your improvements  
4. Submit a Pull Request 🎬

---

## 📜 License

MIT License © 2025 [ssmool](https://github.com/ssmool)

**Example: Setting the Environment Variable (Linux/macOS)**

```bash
export CINEWIZ_API_KEY="[YOUR_GENERATIVE_AI_API_KEY]"
```

**Example: Setting the Environment Variable (Windows)**

```bash
set CINEWIZ_API_KEY="[YOUR_GENERATIVE_AI_API_KEY]"
```

## 📖 Usage

The core functionality resides in the `cinewiz.py` script and the imported functions.

### Command Line Interface (CLI)

You can use `cinewiz.py` directly from the command line for quick image generation:

```bash
python cinewiz.py --prompt "A futuristic cityscape with neon lights and flying cars, digital art" --output "cityscape.png" --size 1024x1024
```

\*— *Adjust the arguments (`--prompt`, `--output`, `--size`) to match your script's actual CLI implementation.*

### Python Library Integration

Import the main generation function into your Python project.

**`example.py`**

```python
import os
from cinewiz import generate_image

# The generate_image function will automatically look for the API key 
# in your environment variables.

prompt = "A majestic lion wearing a crown, sitting on a throne, cinematic lighting."
output_path = "lion_king_genai.jpg"

print(f"Generating image for prompt: '{prompt}'...")

try:
    # Assuming generate_image returns the file path or success status
    result_path = generate_image(
        prompt=prompt,
        size="1024x1024",  # Specify output resolution
        style="cinematic",   # Optional styling parameter
        output_file=output_path
    )
    
    print(f"✅ Image successfully saved to: {os.path.abspath(result_path)}")

except Exception as e:
    print(f"❌ An error occurred during image generation: {e}")

```

\*— *Update `generate_image` function arguments and return values to match `cinewiz.py`.*

## 🤝 Contributing

We welcome contributions to **cinewiz**\! If you have suggestions, bug reports, or want to contribute code, please:

1.  **Fork** the repository.
2.  **Clone** your fork.
3.  Create a new **branch** (`git checkout -b feature/new-feature`).
4.  Make your **changes**.
5.  **Commit** your changes (`git commit -m 'feat: Add new feature X'`).
6.  **Push** to the branch (`git push origin feature/new-feature`).
7.  Open a **Pull Request** to the `main` branch of `ssmool/cinewiz`.

## 📄 License

This project is licensed under the **[CREATIVE COMMONS LICENCSE](../README.md/tree/main?tab=CC0-1.0-1-ov-file#readme)** - see the [LICENSE](https://en.wikipedia.org/wiki/Creative_Commons_license) file for details.

```
```


