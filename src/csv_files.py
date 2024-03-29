import glob
import os
import chardet

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

# LIsta apenas arquivos .csv na pasta 'csv_files'
arquivos_xlsx = glob.glob(os.path.join(input_folder, '*.xlsx'))


def create_folders():
    try:
        # Verifica se a pasta 'csv_files' existe
        if not os.path.exists(csv_files_path):
            # Se não existe, cria a pasta
            os.makedirs(csv_files_path)
            print(f'A pasta "{csv_files_path}" foi criada com sucesso.')
        else:
            print(f'A pasta "{csv_files_path}" já existe.')
            pass

        if not os.path.exists(output_folder) or not os.path.exists(input_folder):
            # Se não existem, cria as pastas
            os.makedirs(input_folder)
            os.makedirs(output_folder)
            print("As pastas foram criadas com sucesso.")
        else:
            print("As pastas já existem.")
            pass

        return True
    except Exception as e:
        print(f"Ocorreu um erro ao criar as pastas: {str(e)}")
        return False


def listar_arquivos_csv():
    if not arquivos_csv:
        print("A pasta 'csv_files' está vazia")
        return False
    else:
        print("\nArquivos na pasta 'csv_files:'")
        for i, arquivo in enumerate(arquivos_csv, start=1):
            print(f"{i}. {arquivo}")
            total = i
        print(f"Total de {total} arquivos")
        print("\nO que deseja fazer com os arquivos acima?")
        return True

def detectar_delimitador(arquivo_csv):
    encoding = detectar_encoding(arquivo_csv)

    # Tenta detectar automaticamente o delimitador olhando para as primeiras 2 linhas do arquivo.
    with open(arquivo_csv, 'r', encoding=encoding) as file:
        primeira_linha = file.readline()
        segunda_linha = file.readline()

    # Lista de delimitadores a serem verificados
    delimitadores = [';', ',', '\t', '|']  # Adicione outros delimitadores, se necessário

    for delimitador in delimitadores:
        if primeira_linha.count(delimitador) > 1 or segunda_linha.count(delimitador) > 1:
            return delimitador

    # Se não foi possível detectar automaticamente, você pode especificar o delimitador manualmente.
    return ','  # Substitua pelo delimitador correto se necessário.

# Função para detectar o encoding correto de um arquivo CSV
def detectar_encoding(arquivo_csv):
    # Detecta o encoding usando a biblioteca chardet
    with open(arquivo_csv, 'rb') as f:
        resultado = chardet.detect(f.read())
    
    # Retorna o encoding detectado
    return resultado['encoding']

# # Junta o nome dos arquivos o com o diretório
# def lista_caminho_dos_csv():
#     caminhos_arquivos = [os.path.join(csv_files_path, arquivo) for arquivo in arquivos_csv]
#     return caminhos_arquivos

# print(arquivos_csv)

# primeiro_arquivo_csv = arquivos_csv[0]
# delimitador_detectado = detectar_delimitador(primeiro_arquivo_csv)
# encoding_dectado = detectar_encoding(primeiro_arquivo_csv)
# print(f"Delimitador detectado para '{primeiro_arquivo_csv}': {delimitador_detectado}")
# print(f"Encoding detectado para '{primeiro_arquivo_csv}': {encoding_dectado}")