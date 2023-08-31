import os
import pandas as pd
import csv

import csv_files

arquivos_csv = csv_files.arquivos_csv

input_folder = csv_files.input_folder
output_folder = csv_files.output_folder



    # for arquivo in arquivos_csv:
    #     with open(arquivo, 'r') as file:
    #         lines = file.readlines()
    #         print(len(lines))

def number_lists(arquivos_csv):
    for arquivo in arquivos_csv:
        with open(arquivo, 'r') as file:
            lines = file.readlines()
            lines_total.extend(lines)
            files.append(arquivo)
    return len(lines_total) or 0



import os
import pandas as pd


def detectar_delimitador(arquivo_csv):
    # Tenta detectar automaticamente o delimitador olhando para as primeiras 2 linhas do arquivo.
    with open(arquivo_csv, 'r') as file:
        primeira_linha = file.readline()
        segunda_linha = file.readline()
    
    if ';' in primeira_linha:
        return ';'
    elif ',' in primeira_linha:
        return ','
    elif ';' in segunda_linha:
        return ';'
    elif ',' in segunda_linha:
        return ','
    else:
        # Se não foi possível detectar automaticamente, você pode especificar o delimitador manualmente.
        return ','  # Substitua pelo delimitador correto se necessário.

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

def unificar_csv(input_folder, output_folder, arquivos_csv, max_linhas_por_arquivo=999999):
    # Verifica se a pasta de saída existe, se não, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Inicializa uma lista para armazenar os DataFrames combinados
    combined_dfs = []
    linha_atual = 0  # Contador de linhas
    ultimo_arquivo_lido = None
    cabecalho_salvo = None
    
    for csv_file in arquivos_csv:
        try:
            # Detecta automaticamente o delimitador correto para este arquivo
            delimitador = detectar_delimitador(csv_file)
            
            # Lê o cabeçalho do primeiro arquivo e salva-o
            if cabecalho_salvo is None:
                with open(csv_file, 'r') as file:
                    cabecalho_salvo = file.readline()
                salvar_cabecalho(csv_file, cabecalho_salvo)
            
            # Lê cada arquivo CSV em um DataFrame, ignorando o cabeçalho e usando o delimitador correto
            df = pd.read_csv(csv_file, delimiter=delimitador, header=None, skiprows=1)
            
            # Verifica se a adição deste DataFrame excederá o limite de linhas
            if linha_atual + len(df) > max_linhas_por_arquivo:
                # Se sim, salve o arquivo atual e comece um novo
                arquivo_saida = os.path.join(output_folder, f'combined_{len(combined_dfs)}.csv')
                combined_df = pd.concat(combined_dfs, ignore_index=True)
                combined_df.to_csv(arquivo_saida, index=False, header=False)
                combined_dfs = []
                linha_atual = 0
            
            combined_dfs.append(df)
            linha_atual += len(df)
            ultimo_arquivo_lido = csv_file
        except Exception as e:
            # Se ocorrer um erro ao ler o arquivo CSV, imprima o arquivo e o erro específico
            print(f"Erro ao processar o arquivo: {csv_file}")
            print(f"Erro específico: {e}")
    
    # Salve o último arquivo se houver dados restantes
    if combined_dfs:
        arquivo_saida = os.path.join(output_folder, f'combined_{len(combined_dfs)}.csv')
        combined_df = pd.concat(combined_dfs, ignore_index=True)
        combined_df.to_csv(arquivo_saida, index=False, header=False)
    
    # # Adicione o cabeçalho ao arquivo resultante
    # arquivo_resultante = os.path.join(output_folder, 'combined.csv')
    # with open(arquivo_resultante, 'w') as file:
    #     file.write(cabecalho_salvo)
    #     with open(arquivo_saida, 'r') as arquivo_saida:
    #         # Ignora a primeira linha (cabeçalho) no arquivo de saída
    #         next(arquivo_saida)
    #         file.write(arquivo_saida.read())
    
    print("Arquivos CSV foram unificados com sucesso.")
    print(f"Último arquivo incluído no arquivo: {ultimo_arquivo_lido}")

unificar_csv(input_folder, output_folder, arquivos_csv)