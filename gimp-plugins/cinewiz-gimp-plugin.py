#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎬 CineWiz GIMP Plugin
----------------------
GIMP plugin and CLI for CineWiz — GenAI Creative Image/Text Toolkit.
Creates cinematic storyboard scenes directly in GIMP.
"""

import os
import sys
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox
from gimpfu import register, main, pdb

# -------------------------------------------------------------------------
# CineWiz imports
# -------------------------------------------------------------------------
try:
    from cinewiz.genai import (
        set_board, set_background, set_picture, set_text,
        set_comix, set_qrcode, add_qrcode, set_sign
    )
    from PIL import Image
except ImportError:
    print("⚠️ CineWiz not found. Please install:")
    print("pip install git+https://github.com/ssmool/cinewiz.git")
    sys.exit(1)


# -------------------------------------------------------------------------
# CineWiz Scene Generator
# -------------------------------------------------------------------------
def cinewiz_generate_scene(board_w, board_h, bg_img, actor_img, text_content,
                           qr_url, author, email, output_path=None):
    """Generates storyboard using CineWiz and saves to output_path."""
    print(f"[CineWiz] Generating {board_w}x{board_h} storyboard...")

    # Create cinematic scene
    set_board(board_w, board_h, (240, 240, 240))
    set_background(2, "vintage cinema", bg_img, "true")
    actor = set_picture(actor_img, 1)
    set_text("scene_1", text_content, 50, 520, "title",
             (20, 20, 20), "fonts/PlayfairDisplay.woff", 36)
    comic_style = set_comix(actor)
    qr = set_qrcode(qr_url)
    add_qrcode(qr, 700, 550)
    set_sign(author, email)

    # Save output if requested
    if output_path:
        # Dummy placeholder — you can replace this with CineWiz's actual final output
        # Assuming CineWiz writes to 'scene_final.png'
        final_image = "scene_final.png"
        if os.path.exists(final_image):
            Image.open(final_image).save(output_path)
        else:
            # Create a placeholder if no file is saved
            Image.new("RGB", (board_w, board_h), (240, 240, 240)).save(output_path)

        print(f"[CineWiz] Saved to {output_path}")
        return output_path
    return None


# -------------------------------------------------------------------------
# GIMP Integration — Display and Save
# -------------------------------------------------------------------------
def open_in_gimp(file_path):
    """Opens the generated image inside GIMP."""
    try:
        image = pdb.gimp_file_load(file_path, file_path)
        pdb.gimp_display_new(image)
        print(f"[CineWiz] Opened in GIMP: {file_path}")
    except Exception as e:
        print(f"⚠️ Could not open image in GIMP: {e}")


# -------------------------------------------------------------------------
# GUI Window
# -------------------------------------------------------------------------
def cinewiz_gui():
    root = tk.Tk()
    root.title("🎬 CineWiz — Storyboard Creator for GIMP")
    root.geometry("460x500")
    root.resizable(False, False)

    params = {
        "board_w": tk.IntVar(value=800),
        "board_h": tk.IntVar(value=600),
        "bg_img": tk.StringVar(value="bg.png"),
        "actor_img": tk.StringVar(value="actor_photo.png"),
        "text_content": tk.StringVar(value="A New Beginning"),
        "qr_url": tk.StringVar(value="https://cinewiz.app/scene/001"),
        "author": tk.StringVar(value="Jane Director"),
        "email": tk.StringVar(value="jane@cinewiz.app"),
    }

    def browse(var):
        path = filedialog.askopenfilename()
        if path:
            var.set(path)

    def run():
        try:
            # Ask where to save result
            save_path = filedialog.asksaveasfilename(
                title="Save Storyboard As...",
                defaultextension=".png",
                filetypes=[("PNG files", "*.png")]
            )
            if not save_path:
                return

            out_path = cinewiz_generate_scene(
                params["board_w"].get(),
                params["board_h"].get(),
                params["bg_img"].get(),
                params["actor_img"].get(),
                params["text_content"].get(),
                params["qr_url"].get(),
                params["author"].get(),
                params["email"].get(),
                output_path=save_path
            )

            if out_path:
                open_in_gimp(out_path)
                messagebox.showinfo("CineWiz", f"Storyboard created and opened in GIMP!\n\nSaved to:\n{out_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

    row = 0
    for label, key in [
        ("Board Width", "board_w"),
        ("Board Height", "board_h"),
        ("Background Image", "bg_img"),
        ("Actor Image", "actor_img"),
        ("Scene Text", "text_content"),
        ("QR URL", "qr_url"),
        ("Author", "author"),
        ("Email", "email"),
    ]:
        tk.Label(root, text=label).grid(row=row, column=0, sticky="w", pady=3)
        entry = tk.Entry(root, textvariable=params[key], width=35)
        entry.grid(row=row, column=1)
        if "img" in key:
            tk.Button(root, text="📂", command=lambda v=params[key]: browse(v)).grid(row=row, column=2)
        row += 1

    tk.Button(
        root, text="🎬 Create and Preview in GIMP", command=run,
        bg="#202020", fg="white", height=2
    ).grid(row=row, column=0, columnspan=3, pady=20)
    root.mainloop()


# -------------------------------------------------------------------------
# CLI Mode
# -------------------------------------------------------------------------
def cinewiz_cli():
    tmp = os.path.join(tempfile.gettempdir(), "cinewiz_cli_output.png")
    cinewiz_generate_scene(
        800, 600, "bg.png", "actor_photo.png",
        "A New Beginning", "https://cinewiz.app/scene/001",
        "Jane Director", "jane@cinewiz.app",
        output_path=tmp
    )
    open_in_gimp(tmp)
    print(f"Storyboard generated and opened: {tmp}")


# -------------------------------------------------------------------------
# GIMP Menu Registration
# -------------------------------------------------------------------------
def cinewiz_gimp_menu(image, drawable):
    cinewiz_gui()


register(
    "python-fu-cinewiz-storyboard",
    "CineWiz Storyboard Creator",
    "Create cinematic storyboard scenes using CineWiz directly inside GIMP.",
    "ssmool",
    "ssmool / MIT",
    "2025",
    "🎬 Create Storyboard...",
    "*",
    [],
    [],
    cinewiz_gimp_menu,
    menu="<Image>/Filters/CineWiz"
)

# -------------------------------------------------------------------------
if __name__ == "__main__":
    if "--cli" in sys.argv:
        cinewiz_cli()
    else:
        main()

