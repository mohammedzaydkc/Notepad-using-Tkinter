import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(parent=root, mode='r')
    if file:
        content = file.read()
        text_area.insert(1.0, content)
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()

def exit():
    if messagebox.askokcancel("Exit", "Do you really want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Notepad")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

text_area = tk.Text(root)
text_area.pack(fill=tk.BOTH, expand=1)

root.mainloop()