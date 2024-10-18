import tkinter as tk
from tkinter import ttk

def main_screen():
    main_window = tk.Tk()
    main_window.title("Tela Principal")
    
    # Tabela (Treeview)
    tree = ttk.Treeview(main_window, columns=('Nome', 'Função', 'Disponibilidade'), show='headings')
    tree.heading('Nome', text='Nome')
    tree.heading('Função', text='Função')
    tree.heading('Disponibilidade', text='Disponibilidade')

    # Inserindo dados de exemplo
    tree.insert('', tk.END, values=('João', 'Câmera 1', 'Domingo'))
    tree.insert('', tk.END, values=('Maria', 'Repórter', 'Sábado'))
    tree.insert('', tk.END, values=('Pedro', 'Fotos', 'Quarta'))

    tree.pack(fill=tk.BOTH, expand=True)
    main_window.geometry("400x300")
    main_window.mainloop()
