import os

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('~/Documents')

# Concatena o caminho completo com o nome da pasta 'csv_files'
csv_files_path = os.path.join(documents_path, 'csv_files')

# LIsta os arquivos na pasta 'csv_files'
arquivos_csv = os.listdir(csv_files_path)

print(documents_path)
print(csv_files_path)
print(arquivos_csv)