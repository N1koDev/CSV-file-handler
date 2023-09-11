import pandas as pd
import os
import glob

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('~\Documents')

# Concatena o caminho completo com o nome da pasta 'csv_files'
csv_files_path = os.path.join(documents_path, 'csv_files')

# Concatena o caminho completo com o nome da pasta 'input'
input_folder = os.path.join(csv_files_path, 'input')

# Concatena o caminho completo com o nome da pasta 'output'
output_folder = os.path.join(csv_files_path, 'output')

# LIsta apenas arquivos .csv na pasta 'csv_files'
arquivos_csv = glob.glob(os.path.join(input_folder, '*.csv'))

# Especifique o caminho do arquivo CSV que você deseja ler
caminho_arquivo = arquivos_csv[1]

# Use a função read_csv() para ler o arquivo CSV e armazenar os dados em um DataFrame
df = pd.read_csv(caminho_arquivo, error_bad_lines=False)

# Agora você pode usar o DataFrame 'df' para manipular e analisar os dados CSV
# Por exemplo, você pode imprimir as primeiras 5 linhas do DataFrame assim:
print(df.head())