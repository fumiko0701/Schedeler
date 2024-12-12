import os
import sys
from src.check_updates import prompt_for_update
from src.login_screen import login_screen
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.withdraw()

    update_available = prompt_for_update(root)

    if login_screen(root):
        open_main_screen(root)

def open_main_screen(root):
    from src.main_screen import main_screen
    root.deiconify()
    root.protocol("WM_DELETE_WINDOW", on_close)
    main_screen(root)

def on_close():
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()
        exit()

if __name__ == "__main__":
    main()