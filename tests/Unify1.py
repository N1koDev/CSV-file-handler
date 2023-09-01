import os
import pandas as pd

import csv_files

arquivos_csv = csv_files.arquivos_csv

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

def exclui_cabecalho():
    # Lista todos os arquivos no diretório especificado
    arquivos_no_diretorio = os.listdir(input_folder)

    # Filtra os arquivos que são arquivos de texto (.txt) e os exclui
    for arquivo in arquivos_no_diretorio:
        if arquivo.endswith('_cabecalho.txt'):
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

def salvar_dataframe_csv(dataframe, output_folder, file_init, cabecalho):
    arquivo_saida = os.path.join(output_folder, f'combined_{file_init}.csv')
    print(f'Salvando arquivo em: {arquivo_saida}')

    # Salvar o DataFrame em um arquivo CSV sem o cabeçalho
    dataframe.to_csv(arquivo_saida, index=False, header=False)

    # Adicionar o cabeçalho separadamente
    if cabecalho:
        inserir_cabecalho_em_csv(cabecalho, arquivo_saida)

def unificar_csv(input_folder, output_folder, arquivos_csv, max_linhas_por_arquivo=999999):
    
    # Inicializa uma lista para armazenar os DataFrames combinados
    combined_dfs = []
    linha_atual = 0  # Contador de linhas
    ultimo_arquivo_lido = None
    cabecalho_salvo = None
    
    for csv_file in arquivos_csv:
        try:
            delimitador = csv_files.detectar_delimitador(csv_file)

            # Lê o cabeçalho do primeiro arquivo e salva-o
            if cabecalho_salvo is None:
                with open(csv_file, 'r') as file:
                    cabecalho_salvo = file.readline()
                salvar_cabecalho(csv_file, cabecalho_salvo)
            
            # Lê cada arquivo CSV em um DataFrame, ignorando o cabeçalho
            df = ler_dataframe_csv(csv_file, delimitador)
            
            # Verifica se a adição deste DataFrame excederá o limite de linhas
            if linha_atual + len(df) > max_linhas_por_arquivo:
                # Se sim, salve o arquivo atual e comece um novo
                salvar_dataframe_csv(pd.concat(combined_dfs, ignore_index=True), output_folder, len(combined_dfs), cabecalho_salvo)
                combined_dfs = []
                linha_atual = 0
            
            combined_dfs.append(df)
            linha_atual += len(df)
            ultimo_arquivo_lido = csv_file
        except Exception as e:
            # Se ocorrer um erro ao ler o arquivo CSV, imprima o arquivo e o erro específico
            print(f"Erro ao processar o arquivo: {csv_file}")
            print(f"Erro específico: {e}")

    # Salve o último arquivo CSV
    salvar_dataframe_csv(pd.concat(combined_dfs, ignore_index=True), output_folder, len(combined_dfs), cabecalho_salvo)
    
    print("Arquivos CSV foram unificados com sucesso.")
    print(f"Último arquivo incluído no arquivo: {ultimo_arquivo_lido}")

unificar_csv(input_folder, output_folder, arquivos_csv, max_linhas_por_arquivo=999999)