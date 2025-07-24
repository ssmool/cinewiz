Here is a **user manual in English** for the `cinewiz` Python package, formatted like official documentation and including a **bash example** at the end.

---

# 📘 Cinewiz User Manual

**Cinewiz** is a Python package designed to accelerate the creative workflow by enabling **generative text**, **retrieval-augmented generation (RAG)**, and **generative image composition**. It can be integrated into projects involving web crawling, LLM prompt globalization, visual storytelling, and content automation.

---

## 📦 Installation

```bash
pip install cinewiz
```

Or from source:

```bash
git clone https://github.com/ssmool/cinewiz.git
cd cinewiz
pip install .
```

---

## 🔧 Requirements

* Python 3.7+
* `requests`, `Pillow`, `beautifulsoup4`, `pandas`
* Web access for RAG and crawling-based operations

---

## 🌐 GitHub Repository

[https://github.com/ssmool/cinewiz](https://github.com/ssmool/cinewiz)

---

## ✨ Features Overview

| Function                                    | Description                                               |
| ------------------------------------------- | --------------------------------------------------------- |
| `set_init(filename)`                        | Sets the name of the canvas/image file (e.g. "new\.png")  |
| `set_lang(lang_code)`                       | Sets default language (e.g. `en`, `pt`, `fr`)             |
| `add_read_lib_uri(uri)`                     | Adds a web URI for **textual RAG** crawling               |
| `add_read_lib(uri)`                         | Adds a web URI for **image RAG** crawling                 |
| `set_picture(image_file)`                   | Loads an image collection from a file                     |
| `set_board(width, height, rgb)`             | Initializes a blank canvas with size and background color |
| `set_text(text, x, y, format, color)`       | Adds styled text to the canvas                            |
| `set_text_inri(keywords, lang)`             | Uses LLM to generate text from a keyword or .txt          |
| `set_glob_lang(lang, text)`                 | Translates a string to the desired language               |
| `search_image(keyword, use_lib_flag, x, y)` | Searches and adds an image based on keyword               |
| `search_data(keyword, lib_index)`           | Crawls text content by keyword from the URI list          |
| `set_background(keyword)`                   | Adds background using image crawling                      |
| `set_comix(output_name)`                    | Cartoonizes the image based on current canvas             |
| `set_qrcode(url)`                           | Generates a QR code from a string or URL                  |
| `add_qrcode(qr_image, x, y)`                | Inserts the QR code image into the canvas                 |
| `set_sign(author, email)`                   | Signs the image with author metadata                      |

---

## 💡 Example: Bash Usage with `cinewiz`

You can create an image with text, QR code, and a background using the following Python commands in a terminal (assuming `cinewiz` is installed and available):

```bash
python3
```

```python
from cinewiz import *

# Initialize the canvas
set_init("my_creation.png")
set_board(800, 600, "255,255,255")

# Set the working language
set_lang("en")

# Add a text block
set_text("Hello, World!", 100, 100, "multiline_text,left", "0,0,0")

# Add background by keyword
add_read_lib("https://www.pinterest.com/search/pins/?q=#0x00_nature")
set_background("nature")

# Generate and insert QR code
_qr = set_qrcode("https://github.com/ssmool/cinewiz")
add_qrcode(_qr, 600, 500)

# Sign the image
set_sign("cinewiz #genai", "support@cinewiz.dev")

# Save and exit
print("Image created as 'my_creation.png'")
```

---

## 📚 Use Cases

* **AI storytelling** with images and prompts
* **LLM prompt augmentation** using multilingual scaffolding
* **RAG pipelines** for educational or creative retrieval workflows
* **Visual report generators** and image annotation
* **Comics and cartoon stylization**

---

## 🔐 License

MIT License © 2025 - [ssmool](https://github.com/ssmool)

---

## 📚 CINEWIZ - COMMAND LINE FOR RAG AND LLMs BY GEN-AI ENGINERING SOFTWARE BASED ##
## ************************************************************************** ##

by: #asytrick

email: eusmool@gmail.com

git: github.com/ssmool/cinewiz

ver: 1.0 BETA #

stage: underconstruction

Platform: python 3+
