import requests
import zipfile
import os

def check_for_updates():
    repo_url = 'https://api.github.com/repos/escmidadtab/Schedeler/releases/latest'
    response = requests.get(repo_url)
    
    if response.status_code != 200:
        print("Erro ao acessar o repositório.")
        return
    
    latest_release = response.json()
    latest_version = latest_release['tag_name']
    
    # Compare com a versão atual
    current_version = 'v1.0.0'  # Atualize isso sempre que fizer uma nova versão
    
    if latest_version != current_version:
        print(f"Atualização disponível: {latest_version}")
        
        # Baixar o arquivo zip da versão mais recente
        for asset in latest_release['assets']:
            if asset['name'].endswith('.zip'):
                download_url = asset['url']
                headers = {'Accept': 'application/octet-stream'}
                download_response = requests.get(download_url, headers=headers)
                
                with open(f'{latest_version}.zip', 'wb') as f:
                    f.write(download_response.content)
                    
                print("Atualização baixada.")
                
                # Lógica para extrair o zip (se necessário)
                # with zipfile.ZipFile(f'{latest_version}.zip', 'r') as zip_ref:
                #     zip_ref.extractall('diretorio_de_destino')

                # Lógica para instalação pode ir aqui
                break
    else:
        print("Seu programa está atualizado.")
