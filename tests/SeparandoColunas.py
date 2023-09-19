import pandas as pd
import os
import glob
import detectar_encoding  # Correção da importação
import separador

# Obtém o caminho completo para a pasta 'Documents' no diretório padrão do usuário
documents_path = os.path.expanduser('~\Documents')

# Concatena o caminho completo com o nome da pasta 'csv_files'
csv_files_path = os.path.join(documents_path, 'csv_files')

# Concatena o caminho completo com o nome da pasta 'input'
input_folder = os.path.join(csv_files_path, 'input')

# Concatena o caminho completo com o nome da pasta 'output'
output_folder = os.path.join(csv_files_path, 'output')

# Lista apenas arquivos .csv na pasta 'input'
arquivos_csv = glob.glob(os.path.join(input_folder, '*.csv'))

# Verifica se há pelo menos um arquivo CSV na lista
if arquivos_csv:
    # Especifique o caminho do arquivo CSV que você deseja ler (por exemplo, o segundo arquivo)
    caminho_arquivo = arquivos_csv[0]

    # Detectar o encoding do arquivo CSV
    encoding = detectar_encoding.detectar_encoding(caminho_arquivo)

    # Detectar o delimitador do arquivo CSV
    sep = separador.detectar_delimitador(caminho_arquivo)

    # Use a função read_csv() para ler o arquivo CSV e armazenar os dados em um DataFrame
    df = pd.read_csv(caminho_arquivo, encoding=encoding, sep=sep)

    # Dividir a coluna 'Data/Hora' em 'Data' e 'Hora' usando o espaço como separador
    df[['Data', 'Hora']] = df['Data Trans.'].str.split(' ', n=1, expand=True)

    # Aplicar a formatação desejada
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    df['Hora'] = pd.to_datetime(df['Hora']).dt.strftime('%H:%M:%S')

    # Reorganizar as colunas para colocar 'Data' e 'Hora' no início
    colunas = ['Data', 'Hora'] + [coluna for coluna in df.columns if coluna not in ['Data', 'Hora']]
    df = df[colunas]

    # Exibir o DataFrame resultante
    print(df[['Data', 'Hora']])

    # Caminho do arquivo de saída
    output_file_path = os.path.join(output_folder, 'output.csv')

    # Salvar o DataFrame em um arquivo CSV na pasta de saída
    df.to_csv(output_file_path, index=False, encoding=encoding, sep=sep)

    print(f'Dados salvos em: {output_file_path}')
else:
    print("Nenhum arquivo CSV encontrado na pasta de entrada.")

print(arquivos_csv)