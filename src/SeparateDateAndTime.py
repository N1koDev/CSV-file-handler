import os
import pandas as pd
from dateutil.parser import parser
import csv_files


output_folder = csv_files.output_folder
arquivos_csv = csv_files.arquivos_csv

# Pergunte ao usuário qual coluna contém a data/hora
coluna_data_hora = input("Qual é o nome ou número da coluna que contém Data/Hora? ")

# Verifique se a entrada do usuário é um número e converta para inteiro se necessário
try:
    coluna_data_hora = int(coluna_data_hora)
except ValueError:
    pass

# Crie a pasta de saída se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop através dos arquivos CSV
for arquivo_csv in arquivos_csv:
    # Detecta automaticamente o delimitador
    delimitador = csv_files.detectar_delimitador(arquivo_csv)

    # Detecta o encoding correto do arquivo CSV
    encoding = csv_files.detectar_encoding(arquivo_csv)

    # Leia o arquivo CSV
    df = pd.read_csv(arquivo_csv)

    # Se o usuário forneceu o número da coluna, pegue o nome da coluna correspondente
    if isinstance(coluna_data_hora, int):
        coluna_data_hora = df.columns[coluna_data_hora]

    # Analise a primeira célula da coluna de Data/Hora para identificar o formato
    primeira_celula = df[coluna_data_hora].iloc[0]
    formato_data_hora = parser.parse(primeira_celula).strftime("%Y-%m-%d %H:%M:%S")

    # Imprima o formato identificado
    print(f"Formato de Data/Hora em '{arquivo_csv}': {formato_data_hora}")

    # Salve o arquivo CSV com o formato de Data/Hora no nome
    nome_arquivo_saida = os.path.join(output_folder, f"{formato_data_hora}_{os.path.basename(arquivo_csv)}")
    df.to_csv(nome_arquivo_saida, index=False, delimiter=delimitador, encoding=encoding )