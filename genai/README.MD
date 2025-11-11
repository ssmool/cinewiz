Here’s a clear, well-formatted **README.md manual** for your GitHub project **CineWiz** (repository path: `github.com/ssmool/cinewiz/genai/__init__.py`).
It documents how to use the main functions, their parameters, and return values — organized for developer usability.

---

# 🎬 CineWiz — GenAI Creative Image/Text Toolkit

**CineWiz** is a lightweight Python toolkit for creative image composition and visual storytelling.
It provides methods to generate visual scenes, add text and QR codes, set backgrounds, and integrate AI-driven assets (comics, inri-corpus text, YOLO tags, etc).

---

## 📦 Installation

```bash
pip install git+https://github.com/ssmool/cinewiz.git
```

or

```bash
git clone https://github.com/ssmool/cinewiz.git
cd cinewiz/genai
pip install -r requirements.txt
```

Then import in your Python script:

```python
from cinewiz.genai import *
```

---

## 🧩 Basic Usage Example

```python
# Initialize configuration
set_start_first_use_config()

# Initialize a starting image
set_init("start_image.png")

# Create a new board (canvas)
set_board(1024, 768, (255, 255, 255))  # white background

# Set a portrait background
set_background(1, 'portrait richard avedon', 'file.png', 'false')

# Add a picture and remove background
w = set_picture("actor.png", 1)

# Add text overlay
set_text("guid_001", "Directed by Richard", 200, 600, (0, 0, 0),
         "fonts/Montserrat-Regular.woff", 32)

# Add a QR code linking to your film
qrcode = set_qrcode("https://filmfest.io/cinewiz")
add_qrcode(qrcode, 900, 700)

# Optional: Comic-style render
set_comix("scene_final.png")

# Sign the artwork
set_sign("John Doe", "john@example.com")
```

---

## 🧠 Function Reference

| **Method**                                                                            | **Description**                                    | **Parameters**                                     | **Returns**                   |
| ------------------------------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | ----------------------------- |
| `set_start_first_use_config()`                                                        | Initializes CineWiz for first-time setup.          | None                                               | `None`                        |
| `set_init(_buff_glob_file)`                                                           | Sets the initial base image.                       | `start_image.png` (path)                           | `_buff_glob_file`             |
| `set_lang(_buff_lang_flag)`                                                           | Sets the global language flag for text operations. | Language code (e.g. `'en'`, `'fr'`)                | `_buff_lang_flag`             |
| `add_read_lib_inri_uri(_buff_uri)`                                                    | Adds a URI to the inri-corpus library.             | URI string                                         | `None`                        |
| `add_read_lib(_buff_uri)`                                                             | Adds a generic read library URI.                   | URI string                                         | `None`                        |
| `set_picture(image_file, flag_rmbg)`                                                  | Adds an image; optionally removes background.      | `image_file` (str), `flag_rmbg` (0=keep, 1=remove) | `_w` (processed image buffer) |
| `set_picture_remove_bg(_buff)`                                                        | Removes background from buffer directly.           | `_buff` (image buffer)                             | `_fl_out` (image buffer)      |
| `set_board(siz_x, siz_y, color_rgb)`                                                  | Creates a new canvas/board.                        | Width, Height (px), `(R,G,B)`                      | Canvas buffer                 |
| `set_text(file_name, txt, pos_x, pos_y, format, text_color_rgb, font_ttf, font_size)` | Draws text on the board.                           | File, text, x, y, format, color, font, size        | Rendered text buffer          |
| `set_text_inri(file_name, keywords, glob_lang)`                                       | Creates an INRI text corpus entry.                 | file name, keywords, language                      | `_dbas_txt_coll`              |
| `set_inri_corpus_text_add_lib(_buff)`                                                 | Adds a text corpus entry to the INRI library.      | Text buffer                                        | None                          |
| `get_inri_corpus_text_lib(_file_name)`                                                | Retrieves a corpus text from library.              | File name                                          | `_buff`                       |
| `set_glob_lang(glob_lang_cod, _dbas_txt)`                                             | Sets and applies a global language corpus.         | Language code, text database                       | `_tot_txt_glob_lang`          |
| `get_yolo_config(_buff_glob_fl)`                                                      | Loads YOLO detection configuration.                | Config buffer                                      | None                          |
| `get_yolo_detect_tags(_buff_cc)`                                                      | Gets YOLO object tags from image.                  | Image buffer                                       | `_buff_tag_kpi`               |
| `search_image(key_words, _buff_glob_lib_flag, pos_x, pos_y, flag_rmbg=0)`             | Searches and places images by keyword.             | keywords, lib flag, x, y, remove-bg flag           | `_buff_w`                     |
| `set_file_lib(_buff_data_file)`                                                       | Adds a data file to CineWiz library.               | File buffer                                        | None                          |
| `get_file_lib_name(_file_name)`                                                       | Fetches a stored file name.                        | File name                                          | `_buff`                       |
| `set_data_text_lib(_buff_data_text)`                                                  | Adds a text file to CineWiz data library.          | Text buffer                                        | None                          |
| `get_text_lib_name(_file_name)`                                                       | Fetches a stored text name.                        | File name                                          | `_buff`                       |
| `search_data(key_words, _buff_uri_index)`                                             | Searches for text data entries by keyword.         | Keywords, index buffer                             | `_buff_txt`                   |
| `set_background(type, key_words, _buff_glob_fl, _buff_flag_smx)`                      | Sets image background by style or keyword.         | type (int), keywords, file, flag                   | None                          |
| `set_comix(_buff_glob_data)`                                                          | Converts an image into comic-book style.           | Image buffer                                       | Comic-styled buffer           |
| `set_qrcode(url)`                                                                     | Generates a QR code.                               | URL/text                                           | `_w` (QR image)               |
| `add_qrcode(_w, pos_x, pos_y)`                                                        | Adds generated QR code to image.                   | QR image, X, Y position                            | None                          |
| `set_sign(author, email)`                                                             | Adds digital signature metadata.                   | author name, email                                 | None                          |

---

## 🧰 Extended Example

```python
# Build a creative storyboard scene
set_board(800, 600, (240, 240, 240))
set_background(2, 'vintage cinema', 'bg.png', 'true')
actor_img = set_picture('actor_photo.png', 1)
set_text('scene_1', 'A New Beginning', 50, 520, 'title',
         (20, 20, 20), 'fonts/PlayfairDisplay.woff', 36)
comic_style = set_comix(actor_img)
qr = set_qrcode('https://cinewiz.app/scene/001')
add_qrcode(qr, 700, 550)
set_sign('Jane Director', 'jane@cinewiz.app')
```

---

## 🧾 License

MIT © [ssmool](https://github.com/ssmool)

---

Would you like me to format this README.md in GitHub-ready Markdown (with syntax highlighting, emojis, and code fences for each function section)?
I can also add an **auto-generated function call graph** or **usage flow diagram** if you want a visual appendix.
