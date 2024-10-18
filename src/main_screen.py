import tkinter as tk
from tkinter import messagebox
import sys  # Importar sys para poder encerrar o programa completamente

def main_screen(master):
    master.title("Tela Principal")
    master.geometry("600x400")

    # Define o comportamento ao tentar fechar a janela
    master.protocol("WM_DELETE_WINDOW", lambda: on_closing(master))

    welcome_label = tk.Label(master, text="Bem-vindo à Tela Principal!", font=("Helvetica", 16))
    welcome_label.pack(pady=20)

    # Adicionando um botão para fechar a aplicação
    button_close = tk.Button(master, text="Fechar", command=lambda: on_closing(master), bg='#29524a', fg='white', font=("Helvetica", 12))
    button_close.pack(pady=(20, 0))

def on_closing(master):
    """ Função chamada quando o usuário clica no 'X' para fechar a janela. """
    if messagebox.askokcancel("Fechar", "Tem certeza que deseja fechar o programa?"):
        master.destroy()  # Fecha a janela principal
        sys.exit()  # Encerra o processo completamente
