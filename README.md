## 🎬 Cinewiz - Theatre Movie RAG GEN-AI

![Python CiNEWIZ_RAG_GENAI Logo](./assets/cinewiz_cover.gif)

**Version:** 2.0 Beta

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


Based on your GitHub repository, I've created a comprehensive `README.md` for `cinewiz.py`. This README highlights the creative image generation features from your code, focusing on the Bing search, background removal, and text composition capabilities.

```markdown
# 🎬 CineWiz - AI Image Composer & Text Generator

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/badge/pypi-v1.0-blue.svg)](https://pypi.org/project/cinewiz/)

**CineWiz** is an open-source Python toolkit for creative image composition, AI-powered visual storytelling, and multimodal content generation. It combines Bing image search, automatic background removal, text overlays, and QR code embedding into a single pipeline.

## ✨ Key Features

- 🔍 **Bing Image Search** – Search and download images by keywords (no API key required)
- 🖼️ **Automatic Background Removal** – Uses `rembg` AI to remove backgrounds from any image
- 📝 **Smart Text Parsing** – Separate image keywords from text overlays using quotes
- 🎨 **Grid Composition** – Automatically arranges images in a 3x3 grid layout
- 📊 **Multi-language Support** – Globalize prompts across different languages
- 🔗 **QR Code Integration** – Embed QR codes into your compositions
- 🧠 **RAG Ready** – Designed to work with Retrieval-Augmented Generation pipelines

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ssmool/cinewiz.git
cd cinewiz

# Install dependencies
pip install rembg pillow requests beautifulsoup4
```

### Basic Usage

```python
from cinewiz import main

# Run interactive mode
main()
```

### Command Line Example

```bash
python cinewiz.py
```

Then enter your prompt:
```
cat dog "Hello World" bird "Beautiful Sunset"
```

This will:
1. Search Bing for images: `cat`, `dog`, `bird`
2. Download the first image for each keyword
3. Remove backgrounds from all images
4. Add text overlays: `Hello World` and `Beautiful Sunset`
5. Compose everything into a single PNG file

## 📘 Function Reference

| Function | Description | Parameters |
|----------|-------------|------------|
| `parse_prompt()` | Separates image keywords from text in quotes | `search_query` (str) |
| `BingImageScraper.search_images()` | Searches Bing for images by keyword | `keyword`, `limit` |
| `BingImageScraper.download_image()` | Downloads image from URL | `url`, `keyword` |
| `ImageComposer.add_image()` | Adds image to canvas with optional BG removal | `image_path`, `position`, `size`, `remove_bg` |
| `ImageComposer.add_text()` | Adds text overlay to composition | `text`, `position`, `font_size`, `color` |
| `ImageComposer.save_composition()` | Saves final image as PNG | `filename` |

## 🔄 Usage Flow Diagram

```
┌─────────────────────┐
│  Enter Prompt       │
│  "cat dog 'text'"   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  parse_prompt()     │
│  Split keywords &   │
│  text overlays      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  BingImageScraper   │
│  Search & download  │
│  images by keyword  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  ImageComposer      │
│  Create canvas      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  For each image:    │
│  • Remove background│
│  • Resize           │
│  • Paste to canvas  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Add text overlays  │
│  from quotes        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Save composition   │
│  as PNG file        │
└─────────────────────┘
```

## 🎯 Example Outputs

### Prompt: `mountain beach "Summer Vibes" forest`

Creates a composition with:
- Mountain landscape (background removed)
- Beach scene (background removed)
- Forest image (background removed)
- "Summer Vibes" text overlay

### Prompt: `"Welcome" city night "CineWiz"`

Creates a composition with:
- City night image (background removed)
- "Welcome" text overlay
- "CineWiz" text overlay (with decorative styling)

## 🛠️ Advanced Usage

### Custom Font Support

```python
# Add text with custom font
composer.add_text(
    "Custom Text",
    position=(100, 100),
    font_size=32,
    color=(255, 0, 0),
    font_path="/path/to/font.ttf",
    multiline=True
)
```

### Adjust Image Layout

```python
# Custom grid positions
positions = [
    (0, 0), (640, 0), (1280, 0),
    (0, 360), (640, 360), (1280, 360)
]
image_size = (600, 600)
```

## 📋 Requirements

- Python 3.7+
- Internet connection (for Bing image search)
- Required packages:
  - `rembg` – AI background removal
  - `Pillow` – Image processing
  - `requests` – HTTP requests
  - `beautifulsoup4` – HTML parsing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [Bing Image Search](https://www.bing.com/images) – Image source
- [rembg](https://github.com/danielgatis/rembg) – Background removal
- [Pillow](https://python-pillow.org/) – Image processing
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing

## 📞 Contact & Support

- **GitHub Issues**: [Report a bug](https://github.com/ssmool/cinewiz/issues)
- **Author**: #asytrick
- **Project Link**: [https://github.com/ssmool/cinewiz](https://github.com/ssmool/cinewiz)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ssmool/cinewiz&type=Date)](https://star-history.com/#ssmool/cinewiz&Date)

---

**CineWiz** – Creative AI for Multimedia Content | Open Source | Built in Python 🐍
```

## Key Sections for Your GitHub README

1. **Badges** – Quick status indicators (Python version, license, PyPI)
2. **Key Features** – Visual highlights of what CineWiz can do
3. **Quick Start** – Installation and basic usage
4. **Function Reference** – Table of main functions from your code
5. **Usage Flow Diagram** – ASCII art showing the pipeline
6. **Advanced Usage** – Custom fonts and layout adjustments
7. **Requirements** – Dependencies from your code
8. **Contributing & License** – Open-source essentials

To add this to your repository:

```bash
# Save the README
nano README.md
# Paste the content above

# Add and commit
git add README.md
git commit -m "Add comprehensive README for CineWiz"
git push origin main
```

The README is optimized for GitHub's Markdown rendering and accurately reflects the code we've been working on, including the Bing search, background removal, and text composition features.

## 🔗 License

This project is licensed under the **MIT License**. Feel free to use, adapt, and contribute!

> **Cinewiz** – Creative AI for Multimedia Content, Open Source and Built in Python.

## 📦 CineOS Barsotti @buskplay - RAG PARTS:

Cinewiz is a part of the CineOS Barsotti @buskplay - Unix Like project and aligned with global goals for decentralized AI-assisted creative AI Orquestrators by LLMs and GEN-AI by generative creativity.
