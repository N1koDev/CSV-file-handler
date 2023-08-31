import glob
import os

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('~/Documents')

# Concatena o caminho completo com o nome da pasta 'csv_files'
csv_files_path = os.path.join(documents_path, 'csv_files')

# Concatena o caminho completo com o nome da pasta 'input'
input_folder = os.path.join(csv_files_path, 'input')

# Concatena o caminho completo com o nome da pasta 'output'
output_folder = os.path.join(csv_files_path, 'output')

# LIsta apenas arquivos .csv na pasta 'csv_files'
arquivos_csv = glob.glob(os.path.join(input_folder, '*.csv'))

def create_folders():
    try:
        # Verifica se a pasta 'csv_files' existe
        if not os.path.exists(csv_files_path):
            # Se não existe, cria a pasta
            os.makedirs(csv_files_path)
            # print(f'A pasta "{csv_files_path}" foi criada com sucesso.')
        else:
            # print(f'A pasta "{csv_files_path}" já existe.')
            pass

        if not os.path.exists(output_folder) or not os.path.exists(input_folder):
            # Se não existem, cria as pastas
            os.makedirs(input_folder)
            os.makedirs(output_folder)
            print("As pastas foram criadas com sucesso.")
        else:
            # print("As pastas já existem.")
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

# # Junta o nome dos arquivos o com o diretório
# def lista_caminho_dos_csv():
#     caminhos_arquivos = [os.path.join(csv_files_path, arquivo) for arquivo in arquivos_csv]
#     return caminhos_arquivos

print(arquivos_csv)
