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

def detectar_delimitador(arquivo_csv):
    # Tenta detectar automaticamente o delimitador olhando para as primeiras 2 linhas do arquivo.
    with open(arquivo_csv, 'r') as file:
        primeira_linha = file.readline()
        segunda_linha = file.readline()

    # Lista de delimitadores a serem verificados
    delimitadores = [';', ',', '\t', '|']  # Adicione outros delimitadores, se necessário

    for delimitador in delimitadores:
        if primeira_linha.count(delimitador) > 1 or segunda_linha.count(delimitador) > 1:
            return delimitador

    # Se não foi possível detectar automaticamente, você pode especificar o delimitador manualmente.
    return ','  # Substitua pelo delimitador correto se necessário.

# Diretórios de entrada e saída
input_folder = '/home/nicolas/Documents/csv_files/input'
output_folder = '/home/nicolas/Documents/csv_files/output'

# Função para contar as linhas de um arquivo CSV
def contar_linhas_arquivo_csv(arquivo):
    with open(arquivo) as f:
        return sum(1 for line in f)

# Lista de arquivos CSV no diretório
arquivos_csv = [os.path.join(input_folder, arquivo) for arquivo in os.listdir(input_folder) if arquivo.endswith('.csv')]

# Total de linhas em todos os arquivos CSV
total_linhas = sum(contar_linhas_arquivo_csv(arquivo) for arquivo in arquivos_csv)

# Número máximo de linhas por arquivo de saída
linhas_por_arquivo = 999999

# Lista para armazenar os DataFrames dos arquivos CSV
dataframes = []

# Lê cada arquivo CSV e adiciona ao DataFrame, ignorando erros de análise
for arquivo_csv in arquivos_csv:
    try:
        delimitador = detectar_delimitador(arquivo_csv)
        df = pd.read_csv(arquivo_csv, low_memory=False, delimiter=delimitador)
        dataframes.append(df)
    except Exception as e:
        print(f"Erro ao ler o arquivo {arquivo_csv}: {e}")

# Concatena todos os DataFrames
df_concatenado = pd.concat(dataframes, axis=0, ignore_index=True)

# Divide o DataFrame em grupos de acordo com o número de linhas
grupos_dataframes = [df_concatenado[i:i+linhas_por_arquivo] for i in range(0, len(df_concatenado), linhas_por_arquivo)]

# Cria os arquivos de saída
for i, grupo in enumerate(grupos_dataframes):
    arquivo_saida = os.path.join(output_folder, f'output_{i + 1}.csv')
    grupo.to_csv(arquivo_saida, index=False)

# Exibe informações sobre a operação
print(f'Total de linhas nos arquivos CSV: {total_linhas}')
print(f'Número de arquivos de saída criados: {len(grupos_dataframes)}')
