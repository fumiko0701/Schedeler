import json
import os
import requests
from dotenv import load_dotenv
from colorama import init, Fore

# Inicializa o colorama
init(autoreset=True)

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def check_for_updates(current_version):
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env
    token = os.getenv('GITHUB_TOKEN')  # Substitua pelo nome da variável de ambiente que contém seu token
    repo_url = 'https://api.github.com/repos/escmidadtab/Schedeler/releases/latest'
    
    headers = {
        'Authorization': f'token {token}',  # Autenticação com o token
        'Accept': 'application/vnd.github.v3+json',
    }
    
    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        latest_version = response.json()['tag_name']
        if latest_version != current_version:
            # Exibe a versão atual em vermelho e a nova versão em verde
            print(f"Atualização disponível: {Fore.GREEN}{latest_version}{Fore.RESET} (Versão atual: {Fore.RED}{current_version}{Fore.RESET})")
            return True
    else:
        print(f"Erro ao acessar o repositório: {response.status_code}")
    return False

def prompt_for_update():
    config = load_config()
    current_version = config['version']

    if check_for_updates(current_version):
        download_update = input("Você gostaria de baixar a atualização? (s/n): ")
        if download_update.lower() == 's':
            print("Baixando atualização...")
            # Lógica para baixar e instalar a atualização
        else:
            print("Atualização não baixada.")
