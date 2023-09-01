import os
import csv

import csv_files

def contar_linhas_arquivos_no_diretorio(diretorio):
    total_linhas = 0

    # Lista todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)

        # Verifica se o arquivo é um arquivo CSV
        if nome_arquivo.endswith('.csv'):
            with open(caminho_arquivo, 'r', newline='') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)

                # Pule o cabeçalho
                next(leitor_csv, None)

                # Conte as linhas no arquivo e adicione ao total
                total_linhas += sum(1 for linha in leitor_csv)

    return total_linhas

# Diretório onde os arquivos estão localizados
diretorio = csv_files.input_folder
total_linhas = contar_linhas_arquivos_no_diretorio(diretorio)
print(f"Total de linhas (sem o cabeçalho) em arquivos CSV no diretório {diretorio}: {total_linhas}")

# 1785973