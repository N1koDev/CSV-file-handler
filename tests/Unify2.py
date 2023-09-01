import os
import pandas as pd

import csv_files

# arquivos_csv = csv_files.arquivos_csv

arquivos_csv = '/home/nicolas/Documents/csv_files/input'

input_folder = csv_files.input_folder
output_folder = csv_files.output_folder

def salvar_cabecalho(arquivo_csv, cabecalho):
    # Salva o cabeçalho em um arquivo separado para uso posterior.
    cabecalho_file = arquivo_csv.replace('.csv', '_cabecalho.txt')
    with open(cabecalho_file, 'w') as file:
        file.write(cabecalho)

def ler_cabecalho(arquivo_csv):
    # Lê o cabeçalho salvo de um arquivo.
    cabecalho = ''
    cabecalho_file = arquivo_csv.replace('.csv', '_cabecalho.txt')
    if os.path.exists(cabecalho_file):
        with open(cabecalho_file, 'r') as file:
            cabecalho = file.read()
    return cabecalho

def exclui_cabecallho():
    # Lista todos os arquivos no diretório especificado
    arquivos_no_diretorio = os.listdir(input_folder)

    # Filtra os arquivos que são arquivos de texto (.txt) e os exclui
    for arquivo in arquivos_no_diretorio:
        if arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(input_folder, arquivo)
            os.remove(caminho_arquivo)

def ler_dataframe_csv(csv_file, delimitador):
    # Lê um arquivo CSV em um DataFrame, ignorando o cabeçalho e usando o delimitador correto
    return pd.read_csv(csv_file, delimiter=delimitador, header=None, skiprows=1)


def inserir_cabecalho_em_csv(cabecalho, nome_arquivo_csv):
    # Abrir o arquivo em modo de leitura e salvar seu conteúdo
    with open(nome_arquivo_csv, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()

    # Reabrir o arquivo em modo de escrita e adicionar o cabeçalho
    with open(nome_arquivo_csv, 'w') as arquivo_csv:
        arquivo_csv.write(cabecalho)
        arquivo_csv.writelines(linhas)

def salvar_dataframe_csv(dataframe, output_folder, file_init, file_end, cabecalho):
    arquivo_saida = os.path.join(output_folder, f'combined_{file_init}_{file_end}.csv')
    print(f'Salvando arquivo em: {arquivo_saida}')

    # Salvar o DataFrame em um arquivo CSV sem o cabeçalho
    dataframe.to_csv(arquivo_saida, index=False, header=False)

    # Adicionar o cabeçalho separadamente
    if cabecalho:
        inserir_cabecalho_em_csv(cabecalho, arquivo_saida)

#########################

import os
import pandas as pd


# Função para contar as linhas de um arquivo CSV
def contar_linhas_arquivo_csv(arquivo):
    with open(arquivo) as f:
        return sum(1 for line in f)

# Lista de arquivos CSV no diretório
arquivos_csv = [os.path.join(arquivos_csv, arquivo) for arquivo in os.listdir(arquivos_csv) if arquivo.endswith('.csv')]

# Total de linhas em todos os arquivos CSV
total_linhas = sum(contar_linhas_arquivo_csv(arquivo) for arquivo in arquivos_csv)

# Número máximo de linhas por arquivo de saída
linhas_por_arquivo = 999999

# Lista para armazenar os DataFrames dos arquivos CSV
dataframes = []

# Lê cada arquivo CSV e adiciona ao DataFrame, ignorando erros de análise
for arquivo_csv in arquivos_csv:
    try:
        df = pd.read_csv(arquivo_csv, error_bad_lines=False)
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
