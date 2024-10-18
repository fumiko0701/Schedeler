import requests

def check_for_updates():
    repo_url = 'https://api.github.com/repos/SEU_USUARIO/SEU_REPOSITORIO/releases/latest'
    response = requests.get(repo_url)
    latest_version = response.json()['tag_name']
    
    # Compare com a versão atual (assumindo que você armazene a versão em algum lugar)
    current_version = 'v1.0.0'
    if latest_version != current_version:
        print(f"Atualização disponível: {latest_version}")
        # Lógica para baixar e instalar a atualização
    else:
        print("Seu programa está atualizado.")
