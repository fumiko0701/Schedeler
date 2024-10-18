import json
import os
import requests
import sys
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from colorama import init, Fore
from src.login_screen import *

init(autoreset=True)

def load_config():
    """Carrega o arquivo de configuração e retorna seu conteúdo."""
    try:
        config_path = 'config.json' if not hasattr(sys, '_MEIPASS') else os.path.join(sys._MEIPASS, 'config.json')
        with open(config_path) as config_file:
            return json.load(config_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"{Fore.RED}Erro ao carregar 'config.json': {str(e)}{Fore.RESET}")
        return None

def check_for_updates(current_version):
    """Verifica se há atualizações disponíveis no repositório do GitHub."""
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env
    token = os.getenv('GITHUB_TOKEN')

    if not token:
        print(f"{Fore.RED}Erro: O token do GitHub não está definido.{Fore.RESET}")
        return False

    repo_url = 'https://api.github.com/repos/escmidadtab/Schedeler/releases/latest'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    try:
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        latest_version = response.json()['tag_name']
        if latest_version != current_version:
            print(f"Atualização disponível: {Fore.GREEN}{latest_version}{Fore.RESET} (Versão atual: {Fore.RED}{current_version}{Fore.RESET})")
            return True
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Erro ao acessar o repositório: {e}{Fore.RESET}")

    return False

def ask_for_update():
    """Pergunta ao usuário se deseja atualizar o software."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    return messagebox.askyesno("Atualização Disponível", "Você gostaria de baixar a atualização?")

def prompt_for_update(root):
    """Checa atualizações e pede ao usuário se deseja atualizar."""
    config = load_config()
    if config is None:
        return

    current_version = config.get('version')
    if current_version is None:
        print(f"{Fore.RED}Erro: A versão atual não foi encontrada em 'config.json'.{Fore.RESET}")
        return

    if check_for_updates(current_version):
        if ask_for_update():
            print("Baixando atualização...")
            # Lógica para baixar e instalar a atualização
        else:
            print("Atualização não baixada.")
    
    # Chame a tela de login após a interação de atualização
    login_screen(root)  # Chame a função de login, que agora precisa de um argumento root

if __name__ == "__main__":
    # Não chame mais `show_console()`
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    prompt_for_update(root)  # Passa a instância root para a função
    root.mainloop()  # Mantém a aplicação rodando
