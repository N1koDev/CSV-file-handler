import os
import pandas as pd
import csv_files
from dateutil import parser
from dateutil.parser import ParserError

def infer_date_format(date_str):
    try:
        parser.parse(date_str)
        return True
    except ParserError:
        return False

def standardize_dates(arquivos_csv):
    # Loop pelos arquivos CSV
    for arquivo_csv in arquivos_csv:
        arquivo_path = os.path.join(arquivo_csv)

        # Detecta automaticamente o delimitador
        delimitador = csv_files.detectar_delimitador(arquivo_path)

        # Detecta o encoding correto do arquivo CSV
        encoding = csv_files.detectar_encoding(arquivo_path)

        # Leitura do arquivo CSV com o delimitador detectado
        df = pd.read_csv(arquivo_path, delimiter=delimitador, encoding=encoding)

        # Tenta inferir o formato da coluna de data
        coluna_data = None
        for coluna in df.columns:
            if df[coluna].apply(infer_date_format).all():
                coluna_data = coluna
                break

        if coluna_data is None:
            print(f"Não foi possível inferir o formato da coluna de data no arquivo '{arquivo_csv}'.")
        else:
            # Formata a coluna de data de acordo com o formato inferido
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
            df.to_csv(arquivo_path, index=False, sep=delimitador, encoding=encoding)
            print(f"As informações de data no arquivo '{arquivo_csv}' foram formatadas de acordo com a lógica especificada.")