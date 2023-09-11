# import os
# import pandas as pd

# import csv_files

# # arquivos_csv = csv_files.arquivos_csv

# arquivos_csv = '/home/nicolas/Documents/csv_files/input'

# input_folder = csv_files.input_folder
# output_folder = csv_files.output_folder

# # Função para contar as linhas de um arquivo CSV
# def contar_linhas_arquivo_csv(arquivo):
#     with open(arquivo) as f:
#         return sum(1 for line in f)

# # Lista de arquivos CSV no diretório
# arquivos_csv = [os.path.join(arquivos_csv, arquivo) for arquivo in os.listdir(arquivos_csv) if arquivo.endswith('.csv')]

# # Total de linhas em todos os arquivos CSV
# total_linhas = sum(contar_linhas_arquivo_csv(arquivo) for arquivo in arquivos_csv)

# # Número máximo de linhas por arquivo de saída
# linhas_por_arquivo = 999999

# # Lista para armazenar os DataFrames dos arquivos CSV
# dataframes = []

# # Lê cada arquivo CSV e adiciona ao DataFrame, ignorando erros de análise
# for arquivo_csv in arquivos_csv:
#     try:
#         df = pd.read_csv(arquivo_csv, low_memory=False)
#         dataframes.append(df)
#     except Exception as e:
#         print(f"Erro ao ler o arquivo {arquivo_csv}: {e}")

# # Concatena todos os DataFrames
# df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True)

# # Divide o DataFrame em grupos de acordo com o número de linhas
# grupos_dataframes = [df_concatenado[i:i+linhas_por_arquivo] for i in range(0, len(df_concatenado), linhas_por_arquivo)]

# # Cria os arquivos de saída
# for i, grupo in enumerate(grupos_dataframes):
#     arquivo_saida = os.path.join(output_folder, f'output_{i + 1}.csv')
#     grupo.to_csv(arquivo_saida, index=False)

# # Exibe informações sobre a operação
# print(f'Total de linhas nos arquivos CSV: {total_linhas}')
# print(f'Número de arquivos de saída criados: {len(grupos_dataframes)}')


import os
import pandas as pd

import csv_files

# Número máximo de linhas por arquivo de saída
linhas_por_arquivo = 999999

# Lista para armazenar os DataFrames dos arquivos CSV
dataframes = []

# Variável para armazenar o total de linhas em todos os arquivos CSV
total_linhas = 0

# Função para contar as linhas de um arquivo CSV
def contar_linhas_arquivo_csv(arquivo):
    with open(arquivo) as f:
        return sum(1 for line in f)
    
# Função para detectar o encoding correto de um arquivo CSV
def detectar_encoding(arquivo_csv):
    # Lista de encodings a serem testados
    encodings = ['utf-8', 'latin-1', 'ISO-8859-1']
    
    for encoding in encodings:
        try:
            with open(arquivo_csv, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    
    # Se nenhum encoding funcionar, retorna None
    return None

def unify_csv_files (input_folder, output_folder, arquivos_csv):

    
    # Detecta automaticamente o delimitador
    delimitador = csv_files.detectar_delimitador(arquivos_csv[0])

    # Detecta o encoding correto do arquivo CSV
    encoding = csv_files.detectar_encoding(arquivos_csv[0])

    # Lê cada arquivo CSV e adiciona ao DataFrame
    for arquivo_csv in arquivos_csv:
        encoding = detectar_encoding(arquivo_csv)
        if encoding is not None:
            try:
                delimitador = csv_files.detectar_delimitador(arquivo_csv)
                df = pd.read_csv(arquivo_csv, low_memory=False, delimiter=delimitador, encoding=encoding)
                dataframes.append(df)
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo_csv}: {e}")
        else:
            print(f"Não foi possível detectar o encoding adequado para o arquivo {arquivo_csv}")

    # Verifica se há DataFrames para concatenar
    if dataframes:
        # Concatena todos os DataFrames
        df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True)

        # Divide o DataFrame em grupos de acordo com o número de linhas
        grupos_dataframes = [df_concatenado[i:i+linhas_por_arquivo] for i in range(0, len(df_concatenado), linhas_por_arquivo)]

        # Cria os arquivos de saída
        for i, grupo in enumerate(grupos_dataframes):
            arquivo_saida = os.path.join(output_folder, f'output_{i + 1}.csv')
            grupo.to_csv(arquivo_saida, index=False, sep=delimitador, encoding=encoding)

        # Exibe informações sobre a operação
        print(f'Total de linhas nos arquivos CSV: {total_linhas}')
        print(f'Número de arquivos de saída criados: {len(grupos_dataframes)}')
    else:
        print("Nenhum arquivo CSV válido encontrado para processar.")