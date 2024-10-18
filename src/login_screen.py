import tkinter as tk
from tkinter import messagebox
import sqlite3

def login_screen():
    root = tk.Tk()
    root.title("Login")
    
    # Criação dos componentes de login
    label_username = tk.Label(root, text="Usuário")
    label_username.pack(pady=5)
    
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)
    
    label_password = tk.Label(root, text="Senha")
    label_password.pack(pady=5)
    
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    button_login = tk.Button(root, text="Login", command=lambda: login(entry_username, entry_password, root))
    button_login.pack(pady=20)

    root.geometry("300x200")
    root.mainloop()

def login(username, password, root):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username.get(), password.get()))
    
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        root.destroy()  # Fecha a janela de login
        # Aqui você chama a tela principal
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
    
    conn.close()
