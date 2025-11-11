## 🎬 Cinewiz - Theatre Movie RAG GEN-AI

![Python CiNEWIZ_RAG_GENAI Logo](./assets/cinewiz_cover.gif)

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


## 📦 Installation

Install Cinewiz directly from PyPI:

```bash
pip install git+https://github.com/ssmool/cinewiz.git
````

> Requirements:
>
> * Python 3.7+

## 🚀 Features

* 🎨 Generate **images from prompt keywords**
* 🧠 Integrate with **RAG pipelines** and context databases
* 🌍 Support for **text globalization** and multilingual prompts
* 🔍 Web crawling for content gathering and inspiration
* 🧾 Auto-generate **text compositions** with contextual relevance
* 🖼️ Embed **QR codes** directly into your creative artwork
* 🌐 Configure **URI lists** for persistent generative pipelines
* 💡 Trigger everything from a **single keyword command**


## 📘 Usage Example

CineWiz release a first manual instructions version for RAG Enginering on the [CINEWIZ - USER MANUAL FOR COMMAND LINE WITH PYTHON 3+](./genai/README.MD) for completed and first underconstruction version by several pourposes to LLMs and RAG with GEN-AI capabilities with the intuitive command line python use definition by #asytrick

Perfect ✅ — here’s a **GitHub-ready, fully formatted `README.md`** for your `cinewiz` project with:

* Markdown-enhanced sections
* Syntax-highlighted code blocks
* A function reference table
* A usage flow diagram (ASCII format)

You can copy-paste this directly into your repository at
`cinewiz/README.md`.

---

````markdown
# 🎬 CineWiz — GenAI Creative Image/Text Toolkit

**CineWiz** is a lightweight Python toolkit for creative image composition and visual storytelling.  
It allows you to generate AI-driven visual scenes, overlay text, add QR codes, and create comic-style renders — perfect for filmmakers, designers, and developers.

---

## 📦 Installation

```bash
git clone https://github.com/ssmool/cinewiz.git
cd cinewiz/genai
pip install -r requirements.txt
````

Import CineWiz in your project:

```python
from cinewiz.genai import *
```

---

## 🧠 Quick Start Example

```python
# Initialize configuration for first-time setup
set_start_first_use_config()

# Set initial starting image
set_init("start_image.png")

# Create a new canvas
set_board(1024, 768, (255, 255, 255))  # white background

# Add a portrait background (by style/keyword)
set_background(1, "portrait richard avedon", "file.png", 0) # #use 0 - to websearch is not allowed - [1 - when is decrapetd]

# Place a character and remove its background
actor = set_picture("actor.png", 1) #use 0 - to rembg is not allowed

# Add text overlay
set_text(
    "guid_001",
    "Directed by Richard",
    200,
    600,
    (0, 0, 0),
    "fonts/Montserrat-Regular.woff",
    32
)

# Generate and add a QR code
qr = set_qrcode("https://filmfest.io/cinewiz")
add_qrcode(qr, 900, 700)

# Optional: Apply comic-book filter
set_comix("scene_final.png")

# Sign your work
set_sign("John Doe", "john@example.com")
```

---

## ⚙️ Function Reference

| **Function**                                                          | **Description**                                  | **Parameters**                         | **Returns**          |
| --------------------------------------------------------------------- | ------------------------------------------------ | -------------------------------------- | -------------------- |
| `set_start_first_use_config()`                                        | Initializes CineWiz environment on first launch. | None                                   | `None`               |
| `set_init(_buff_glob_file)`                                           | Loads an initial image or buffer.                | `start_image.png`                      | `_buff_glob_file`    |
| `set_lang(_buff_lang_flag)`                                           | Sets language for text or corpus.                | Language flag (`'en'`, `'fr'`, etc.)   | `_buff_lang_flag`    |
| `add_read_lib_inri_uri(_buff_uri)`                                    | Adds INRI corpus source via URI.                 | `_buff_uri`                            | `None`               |
| `add_read_lib(_buff_uri)`                                             | Adds external read library.                      | `_buff_uri`                            | `None`               |
| `set_picture(image_file, flag_rmbg)`                                  | Loads image, optionally removes background.      | `image_file` (path), `flag_rmbg` (0/1) | `_w` (image buffer)  |
| `set_picture_remove_bg(_buff)`                                        | Removes background directly from buffer.         | `_buff`                                | `_fl_out`            |
| `set_board(width, height, color_rgb)`                                 | Creates new drawing board/canvas.                | Width (px), Height (px), `(R,G,B)`     | Canvas buffer        |
| `set_text(file_name, txt, x, y, format, color, font_file, font_size)` | Writes text onto board.                          | Text and style parameters              | Rendered text buffer |
| `set_text_inri(file_name, keywords, glob_lang)`                       | Builds INRI text dataset.                        | `file_name`, `keywords`, `glob_lang`   | `_dbas_txt_coll`     |
| `set_inri_corpus_text_add_lib(_buff)`                                 | Adds text entry to INRI corpus library.          | `_buff`                                | `None`               |
| `get_inri_corpus_text_lib(_file_name)`                                | Reads text corpus entry.                         | `_file_name`                           | `_buff`              |
| `set_glob_lang(glob_lang_cod, _dbas_txt)`                             | Applies global language corpus.                  | Code, text data                        | `_tot_txt_glob_lang` |
| `get_yolo_config(_buff_glob_fl)`                                      | Loads YOLO object detection configuration.       | Config buffer                          | `None`               |
| `get_yolo_detect_tags(_buff_cc)`                                      | Detects object tags via YOLO model.              | Image buffer                           | `_buff_tag_kpi`      |
| `search_image(key_words, _buff_glob_lib_flag, x, y, flag_rmbg=0)`     | Finds and positions image by keyword.            | keywords, flags, coords                | `_buff_w`            |
| `set_file_lib(_buff_data_file)`                                       | Adds data file to CineWiz library.               | `_buff_data_file`                      | `None`               |
| `get_file_lib_name(_file_name)`                                       | Retrieves library file name.                     | `_file_name`                           | `_buff`              |
| `set_data_text_lib(_buff_data_text)`                                  | Adds data text to library.                       | `_buff_data_text`                      | `None`               |
| `get_text_lib_name(_file_name)`                                       | Retrieves stored text name.                      | `_file_name`                           | `_buff`              |
| `search_data(key_words, _buff_uri_index)`                             | Searches for textual data.                       | keywords, index buffer                 | `_buff_txt`          |
| `set_background(type, key_words, _buff_glob_fl, _buff_flag_smx)`      | Sets or generates background.                    | type, keywords, file, flag             | None                 |
| `set_comix(_buff_glob_data)`                                          | Converts image to comic-style.                   | image buffer                           | Comic image          |
| `set_qrcode(text)`                                                    | Creates QR code image.                           | text or URL                            | `_qrcode`            |
| `add_qrcode(_qrcode, x, y)`                                           | Places QR code on board.                         | `_qrcode`, coordinates                 | `None`               |
| `set_sign(author, email)`                                             | Adds author signature metadata.                  | author name, email                     | None                 |

---

## 🎨 Extended Example

```python
# Create cinematic storyboard scene
set_board(800, 600, (240, 240, 240))
set_background(2, "vintage cinema", "bg.png", 0)
actor_img = set_picture("actor_photo.png", 1)
set_text("scene_1", "A New Beginning", 50, 520, "title",
         (20, 20, 20), "fonts/PlayfairDisplay.woff", 36)
comic_style = set_comix(actor_img)
qr = set_qrcode("https://cinewiz.app/scene/001")
add_qrcode(qr, 700, 550)
set_sign("Jane Director", "jane@cinewiz.app")
```

---

## 🔁 Usage Flow Diagram

```text
 ┌─────────────────────────┐
 │ set_start_first_use_config │
 └──────────────┬──────────┘
                │
                ▼
          ┌───────────────┐
          │ set_init()     │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_board()    │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_background │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_picture()  │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_text()     │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_qrcode()   │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ add_qrcode()   │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_comix()    │
          └──────┬────────┘
                 │
                 ▼
          ┌───────────────┐
          │ set_sign()     │
          └───────────────┘
```

---

## 🧾 License

**MIT License**
Copyright © [ssmool](https://github.com/ssmool)

---

> 💡 *Tip:* For advanced automation, combine CineWiz with YOLO object detection and INRI text corpus functions to create AI-enhanced storyboards, movie covers, and comic scenes.

```

---

Would you like me to add:
- ✅ clickable cross-references to each function’s section (anchor links), and  
- 🧩 auto-generated badges (e.g. build status, license, PyPI version)  

so it looks like a professional open-source project on GitHub?
```


## 💡 Why Cinewiz?

**Cinewiz** is part of a larger creative and modular system called **e-Wally**, which aims to develop a modern **Unix-like environment** for studios, multimedia servers, and content production offices. Its initial version is known as **CineOS Barsotti – Unix Like @buskplay**.

## 🙌 Special Thanks

* 🐍 Thanks to the **Python language** for its power, simplicity, and vibrant community
* 🖼️ Shout-out to the **Pillow library** for enabling rich image manipulation
* 🤝 Ongoing support from the **open-source community** and developers worldwide

## 🔗 License

This project is licensed under the **MIT License**. Feel free to use, adapt, and contribute!

> **Cinewiz** – Creative AI for Multimedia Content, Open Source and Built in Python.

## 📦 CineOS Barsotti @buskplay - RAG PARTS:

Cinewiz is a part of the CineOS Barsotti @buskplay - Unix Like project and aligned with global goals for decentralized AI-assisted creative AI Orquestrators by LLMs and GEN-AI by generative creativity.
