import os
import time

def verificar_ou_criar_pasta_csv():
    # Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
    documents_path = os.path.expanduser('~/Documents')

    # Concatena o caminho completo com o nome da pasta 'csv_files'
    csv_files_path = os.path.join(documents_path, 'csv_files')

    if os.path.exists(csv_files_path):
        print(f"A pasta '{csv_files_path}' já existe.")
    else:
        os.makedirs(csv_files_path)
        print(f"A pasta '{csv_files_path}' foi criada.")

    # Verifica se a pasta 'csv_files' existe
    if os.path.exists(csv_files_path):
        # Lista todos os arquivos na pasta 'csv_files'
        arquivos = os.listdir(csv_files_path)

        if not arquivos:
            print(f"A pasta '{csv_files_path}' está vazia.")
        else:
            print(f"Arquivos em '{csv_files_path}':")
            for arquivo in arquivos:
                print(arquivo)

verificar_ou_criar_pasta_csv()