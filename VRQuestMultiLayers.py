import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_folder(entry):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)

def select_file(entry):
    file_selected = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_selected:
        entry.delete(0, tk.END)
        entry.insert(0, file_selected)

def overlay_images():
    input_folder = entry_input_folder.get()
    overlay_path = entry_overlay_image.get()
    output_folder = entry_output_folder.get()
    
    if not (input_folder and overlay_path and output_folder):
        status_label.config(text="Please select 2 folders and your overlay!", fg="red")
        return
    
    overlay = Image.open(overlay_path).convert("RGBA")
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path).convert("RGBA")
            combined = Image.alpha_composite(image, overlay)
            output_path = os.path.join(output_folder, filename)
            combined.convert("RGB").save(output_path, "PNG")
    
    status_label.config(text="Images processed successfully!", fg="green")

# GUI
root = tk.Tk()
root.title("Image Overlay Tool")

# Title Label
title_label = tk.Label(root, text="Make sure that all your images are the same resolution as your overlay png", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Input Folder
tk.Label(root, text="Image Folder:").grid(row=1, column=0)
entry_input_folder = tk.Entry(root, width=50)
entry_input_folder.grid(row=1, column=1)
tk.Button(root, text="Select", command=lambda: select_folder(entry_input_folder)).grid(row=1, column=2)

# Overlay Image
tk.Label(root, text="Overlay:").grid(row=2, column=0)
entry_overlay_image = tk.Entry(root, width=50)
entry_overlay_image.grid(row=2, column=1)
tk.Button(root, text="Select", command=lambda: select_file(entry_overlay_image)).grid(row=2, column=2)

# Output Folder
tk.Label(root, text="Output Folder:").grid(row=3, column=0)
entry_output_folder = tk.Entry(root, width=50)
entry_output_folder.grid(row=3, column=1)
tk.Button(root, text="Select", command=lambda: select_folder(entry_output_folder)).grid(row=3, column=2)

# Process Button
tk.Button(root, text="Start", command=overlay_images).grid(row=4, column=1, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=5, column=1)

root.mainloop()
