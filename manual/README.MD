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

Would you like this manual exported as a **PDF** or included directly in your GitHub repository as a `README.md`?

## 📚 CINEWIZ - COMMAND LINE FOR RAG AND LLMs BY GEN-AI ENGINERING SOFTWARE BASED ##
## ************************************************************************** ##

## set_init(_buff_glob_file): Configure the new image name to create on the default path execute like a PNG | JPEG | GIF ex:'new.png' ##

## set_lang(_buff_lang_flag): configure default idiom for prompt text like a en | fr | pt | jp | es ##

## add_read_lib_uri(_buff_uri): configure and add URI for webcrawling by GEN-AI and RAG Text Generation or research like 'https://en.wikipedia.org/wiki/Walt_Disney' or 'https://en.wikipedia.org/wiki/#0x00_keyword' - its create a #0x00_keyword a input the keyword for your webcrawling by scaffolding between the dictionaries or lists ##

##add_read_lib(_buff_uri): configure and add URI for webcrawling by GEN-AI and RAG Image Generation or research like 'https://www.pinterest.com/search/pins/?q=#0x00_keyword' or 'https://www.google.com/search?udm=2&q=#0x00_keyword' - its create a #0x00_keyword a input the keyword for your webcrawling by scaffolding between the dictionaries or lists or by set directy URI for image 'https://i0.wp.com/www.parksavers.com/wp-content/uploads/2021/12/Incredicoaster-scaled.jpg?resize=1200%2C800&quality=89&ssl=1' ##

## set_picture(image_file): to set collection by images on the collection seted by image_file for local images or search_images(key_words) return on local path with prefix called by '{image_file}_rag_0x_sx_nbx0.png' ##

## set_board(siz_x,siz_y,color_rgb): configure the canvas stage for image size by width and height set the siz_x for width and siz_y for height and set color_rgb by string separated by comma like '255,255,255' ##

## set_text(txt,pos_x,pos_y,format, text_color_rgb): set and write text on the set_init(_buf_glob_file) file wit pos_x like 0...n for x-axis position or post_y for 0...n fir y-axis position and format pass a string separated by comma like 'multiline_text,{left|center|right}' and set font ttf to write like  _c_att_font_ttf = "arial.ttf" and font-size like  _c_att_font_ttf_size = 10 ##

## set_text_inri(keywords, glob_lang): to generative LLMs text result by cardinal range of generative text by prompt text keywords with params keywords='history of civilization etc and blah blah blah or any text by .txt source file extracted' and return a list array with lenght for verify on the en globalization text ##

## set_glob_lang(glob_lang_cod, _dbas_txt): to translate text by blog_lang_cod like 'fr' to translate for French and _dbas_txt to pass the text string for translate like 'history of video games and blah blah blah' ##

## search_image(key_words, _buff_glob_lib_flag, pos_x, pos_y): to search images by add_read_lib(_buf_uri) library and write to _buf_glob_rag_coll_arr collection and write image to set_init(_buff_glob_file) initialized ##

## search_data(key_words,_buff_uri_index): to webcrawling over webdriver by keyword search with the index of _buf_data_uri configured by add_read_lib_uri(_buff_uri) like '0...n' range of collection get by lenght ##

## set_background(key_words): to add background by add PNG | JPG | GIF local files ot search by search_image set type = 0 for local path image or type = 1 to image_search inner joint _buff_flag_smx = 0...n to array collection lenght for add_read_lib(_buff_lib) list by select the URI to get file source to write a background ##

## set_comix(_buff_glob_data): cartoonize the picture with new file set name by _buff_glob_data = 'new.png' based on the set_init(_buff_glob_file) config file ##

## set_qrcode(url): creaet a qrcode with URI for publish or text content like a GUID code for catalog register and get the result by _w = set_qrcode('http://meet.google.com/example_invite_code_live') ##

## add_qrcode(_w, pos_x, pos_y): write the set_qrcode(url) to set_init(_buff_glob_file) file config to GEN-AI content generated with pos_X = 0...n to x-axis and pos_y = 0...n to y-axis write qrcode generated for printed memory current file proccess ##

## set_sign(author,email): add sing to memory current file writed proccess with your author title like author='cinewiz #genai' and email='example@domain.xyz' ##

## by:#asytrick ##

## email:eusmool@gmail.com ##

## git:github.com/ssmool/cinewiz ##

## ver:1.0 BETA ##
## stage:Underconstruction ##
## Platform:Python 3+ ##
