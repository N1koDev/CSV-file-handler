import glob
import chardet
import os

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('~\Documents')

# Concatena o caminho completo com o nome da pasta 'csv_files'
csv_files_path = os.path.join(documents_path, 'csv_files')

# Concatena o caminho completo com o nome da pasta 'input'
input_folder = os.path.join(csv_files_path, 'input')

# Função para detectar o encoding correto de um arquivo CSV
def detectar_encoding(arquivo_csv):
    # Detecta o encoding usando a biblioteca chardet
    with open(arquivo_csv, 'rb') as f:
        resultado = chardet.detect(f.read())
    
    # Retorna o encoding detectado
    return resultado['encoding']

# Use os.scandir() para listar arquivos diretamente
arquivos_csv = [entry.path for entry in os.scandir(input_folder) if entry.is_file() and entry.name.endswith('.csv')]

# Processa os arquivos CSV
for arquivo_csv in arquivos_csv:
    encoding = detectar_encoding(arquivo_csv)
    print(f'O encoding de {arquivo_csv} é {encoding}')
