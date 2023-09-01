import os
import pandas as pd

import csv_files


# # Diretório onde estão os arquivos CSV
# diretorio = csv_files.input_folder  # Substitua pelo caminho do seu diretório

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

# Diretório onde estão os arquivos CSV
diretorio = csv_files.input_folder  # Substitua pelo caminho do seu diretório

# Lista todos os arquivos CSV no diretório
arquivos_csv = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

# Pergunta ao usuário qual coluna contém as informações de data para todos os arquivos
coluna_data = input("Digite o nome da coluna que contém as informações de data para todos os arquivos: ")

# Loop pelos arquivos CSV
for arquivo_csv in arquivos_csv:
    arquivo_path = os.path.join(diretorio, arquivo_csv)

    # Detecta automaticamente o delimitador
    delimitador = detectar_delimitador(arquivo_path)

    # Leitura do arquivo CSV com o delimitador detectado
    df = pd.read_csv(arquivo_path, delimiter=delimitador)

    # Verifica se a coluna escolhida existe no DataFrame
    if coluna_data not in df.columns:
        print(f"A coluna '{coluna_data}' não foi encontrada no arquivo '{arquivo_csv}'.")
    else:
        # Formata a coluna de data de acordo com o formato detectado
        df[coluna_data] = pd.to_datetime(df[coluna_data], errors='coerce')

        # Verifica se a coluna de data contém informações de hora
        if ' ' in df[coluna_data].astype(str).iloc[0]:
            # Se sim, cria novas colunas para data e hora separadas
            df.insert(0, 'Data', df[coluna_data].dt.strftime('%Y-%m-%d'))
            df.insert(1, 'Hora', df[coluna_data].dt.strftime('%H:%M:%S'))
            df.drop(columns=[coluna_data], inplace=True)
        else:
            df.rename(columns={coluna_data: 'Data'}, inplace=True)

        # Sobrescreve o arquivo CSV original com o delimitador correto
        df.to_csv(arquivo_path, index=False, sep=delimitador)
        print(f"As informações de data no arquivo '{arquivo_csv}' foram formatadas de acordo com a lógica especificada.")