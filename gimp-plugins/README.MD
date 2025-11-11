🧾 INSTALLATION MANUAL — INSTALL.md

# 🎬 CineWiz GIMP Plugin (with GIMP Preview)

## 🧩 Features

- GUI window for easy CineWiz storyboard creation  
- “Save As…” dialog to export final image  
- Opens generated storyboard automatically inside GIMP  
- Also supports CLI mode  

---

## ⚙️ Requirements

- **GIMP 2.10+**
- **Python 3.9+**
- **CineWiz Library**

📁 cinewiz-gimp-plugin.py

Save this in your GIMP plug-ins directory:

Windows:
C:\Users\<you>\AppData\Roaming\GIMP\2.10\plug-ins\cinewiz-gimp-plugin.py

macOS/Linux:
~/.config/GIMP/2.10/plug-ins/cinewiz-gimp-plugin.py

Make executable (Linux/macOS):

```bash
chmod +x ~/.config/GIMP/2.10/plug-ins/cinewiz-gimp-plugin.py
```

Install CineWiz:

```bash
pip install git+https://github.com/ssmool/cinewiz.git
```

📥 Installation

Copy the plugin file:

```bash
cinewiz-gimp-plugin.py
```

to your GIMP plug-ins folder:

```bash
chmod +x ~/.config/GIMP/2.10/plug-ins/cinewiz-gimp-plugin.py
```

🖼️ Using the Plugin in GIMP

Restart GIMP.

Open Filters → CineWiz → 🎬 Create Storyboard...

Fill in your storyboard parameters:

Board Width / Height

Background / Actor images

Text & QR URL

Author & Email

Click 🎬 Create and Preview in GIMP

Choose where to save the file — it will appear directly in a new GIMP window.

💻 Command-Line Mode

You can also run CineWiz without the GIMP GUI:

```bash
python cinewiz-gimp-plugin.py --cli
```

This will generate and open a temporary storyboard in GIMP automatically.

🧠 Tips

If you don’t see the plugin:

Ensure the file is executable (chmod +x)

Restart GIMP

Check Python path: Edit → Preferences → Folders → Plug-ins

Update CineWiz anytime:

```bash
pip install --upgrade git+https://github.com/ssmool/cinewiz.git
```

| Feature     | Mode | Description                             |
| ----------- | ---- | --------------------------------------- |
| GIMP GUI    | 🖼️  | Menu item under Filters → CineWiz       |
| Preview     | 👁️  | Automatically opens finished storyboard |
| Save As     | 💾   | Choose custom save path                 |
| CLI         | 💻   | Run plugin from terminal                |
| Integration | 🔗   | Uses CineWiz functions for compositing  |

MIT License © ssmool


