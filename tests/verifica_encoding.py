import glob
import os
import chardet

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('examples/converter_to_utf8/input')

arquivos = glob.glob(os.path.join(documents_path, '*.csv'))

# Função para verificar o encoding de um arquivo
def detect_file_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            return result['encoding']
    except Exception as e:
        print(f"Erro ao detectar a codificação de {file_path}: {str(e)}")
        return None

# Verificar o encoding de cada arquivo na lista
for arquivo in arquivos:
    encoding = detect_file_encoding(arquivo)
    if encoding:
        print(f"Arquivo: {arquivo}, Encoding atual: {encoding}")