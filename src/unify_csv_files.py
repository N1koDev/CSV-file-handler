import csv_files
import pandas as pd

# Inicializa um DataFrame vazio para armazenar os dados
dados_unificados = pd.DataFrame()

for arquivo in csv_files.arquivos_csvrquivos:
    df = pd.read_csv(arquivo)
    dados_unificados = pd.concat([dados_unificados, df], ignore_index=True)

    # Salva o DataFrame unificado em um novo arquivo CSV
    dados_unificados.to_csv(os.path.join(diretorio, arquivo_saida), index=False)
    print(f'Arquivos CSV unificados e salvos em {os.path.join(diretorio, arquivo_saida)}')