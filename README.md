# Schedeler

Schedeler é uma aplicação desenvolvida para gerenciar tarefas e gerar escalas de trabalho de forma mais fácil e eficiente. Este README fornece instruções sobre como configurar e executar o projeto.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/escmidadtab/Schedeler.git
    cd Schedeler
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

## Configuração

1. Crie um arquivo [`.env`](.env) na raiz do projeto e adicione seu token do GitHub:

    ```env
    GITHUB_TOKEN=seu_token_aqui
    ```

2. Verifique e ajuste as configurações no arquivo [`config.json`](config.json) conforme necessário.

## Execução

Para executar a aplicação, use o seguinte comando:

```sh
python main.py
```

## Funcionalidades

- Gerenciamento de tarefas
- Geração automática de escalas de trabalho
- Verificação automática de atualizações

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.