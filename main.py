import os
import sys
from src.check_updates import prompt_for_update
from src.login_screen import login_screen
import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter

    # Verifica atualizações
    update_available = prompt_for_update(root)  # Passa root para a função

    # Mostra a janela de login e verifica se o login foi bem-sucedido
    if login_screen(root):  # Se o login for bem-sucedido, a função retorna True
        open_main_screen(root)  # Abre a tela principal

def open_main_screen(root):
    from src.main_screen import main_screen  # Importa a função main_screen
    root.deiconify()  # Mostra a janela principal novamente
    root.protocol("WM_DELETE_WINDOW", on_close)  # Adiciona tratamento para o fechamento da janela principal
    main_screen(root)  # Chama a função main_screen

def on_close():
    """Trata o fechamento da janela principal"""
    if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        root.destroy()
        exit()  # Encerra o programa

if __name__ == "__main__":
    main()
