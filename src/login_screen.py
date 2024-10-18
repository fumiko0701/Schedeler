import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from .main_screen import main_screen  # Ajuste para usar o caminho relativo

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.configure(bg='#061208')
        master.geometry("400x300")

        master.protocol("WM_DELETE_WINDOW", self.on_close)  # Adiciona tratamento para o fechamento da janela

        title_label = tk.Label(master, text="S C H E D E L E R", font=("Helvetica", 16, "bold"), bg='#061208', fg='white')
        title_label.pack(pady=(20, 10))

        main_frame = tk.Frame(master, bg='#061208')
        main_frame.pack(pady=20)

        login_frame = tk.Frame(main_frame, bg='#061208')
        login_frame.pack(side=tk.LEFT, padx=(20, 10))

        label_username = tk.Label(login_frame, text="Usuário", bg='#061208', fg='white')
        label_username.pack(anchor='w', pady=2)

        self.entry_username = tk.Entry(login_frame, bd=0, highlightthickness=1, highlightbackground="gray", highlightcolor="blue", font=("Helvetica", 12))
        self.entry_username.pack(pady=2)

        label_password = tk.Label(login_frame, text="Senha", bg='#061208', fg='white')
        label_password.pack(anchor='w', pady=2)

        self.entry_password = tk.Entry(login_frame, show="*", bd=0, highlightthickness=1, highlightbackground="gray", highlightcolor="blue", font=("Helvetica", 12))
        self.entry_password.pack(pady=2)

        button_frame = tk.Frame(login_frame, bg='#061208')
        button_frame.pack(side=tk.RIGHT, pady=10)

        button_login = tk.Button(button_frame, text="Entrar", command=self.verify_login, bg='#29524a', fg='white', font=("Helvetica", 12, "bold"))
        button_login.pack()

        self.load_logo(main_frame)

    def load_logo(self, main_frame):
        logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'logo.png')
        print(f"img path: {logo_path}")

        try:
            self.logo_image = Image.open(logo_path)
            self.logo_image = self.logo_image.resize((80, 150), Image.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            self.logo_label = tk.Label(main_frame, image=self.logo_photo, bg='#061208')
            self.logo_label.image = self.logo_photo  # Mantém a referência da imagem
            self.logo_label.pack(side=tk.RIGHT, padx=(10, 0), pady=(10, 0))

            print("-sucess (001)")

        except FileNotFoundError:
            print("-fail (001)")
        except Exception as e:
            print(f"-fail {e} (002)")

    def verify_login(self):
        user = self.entry_username.get()
        pwd = self.entry_password.get()
        print(f"try _{user}_ and: _{pwd}_")

        if user == "1" and pwd == "1":  # Use suas credenciais reais aqui
            print("-sucess (002)")
            self.open_main_screen()  # Chama a função para abrir a tela principal
        else:
            print("-fail (003)")
            self.show_custom_error("🫠 Nome de usuário ou senha incorretos.")
            return False  # Retorna falso

    def open_main_screen(self):
        # Cria uma nova janela para a tela principal
        main_window = tk.Toplevel(self.master)
        self.master.withdraw()  # Esconde a janela de login
        main_screen(main_window)  # Chama a função main_screen

    def show_custom_error(self, message):
        error_window = tk.Toplevel(self.master)
        error_window.title("Erro")
        error_window.configure(bg='#061208')
        error_window.geometry("300x150")

        error_label = tk.Label(error_window, text=message, bg='#061208', fg='white', font=("Helvetica", 12))
        error_label.pack(pady=20)

        button_close = tk.Button(error_window, text="Fechar", command=error_window.destroy, bg='#29524a', fg='white', font=("Helvetica", 12))
        button_close.pack(pady=(0, 20))

    def on_close(self):
        """Trata o fechamento da janela de login"""
        if messagebox.askokcancel("Sair", "Tem certeza que deseja sair?"):
            self.master.destroy()  # Fecha a janela
            exit()  # Encerra o programa

def login_screen(root):
    app = LoginApp(root)
    root.deiconify()
    root.mainloop()  # Mantém o loop da janela de login
    return app.verify_login()  # Retorna o resultado do login
