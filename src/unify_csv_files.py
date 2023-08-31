import os
import pandas as pd
import csv_files

def unificar_csv(input_folder, output_folder, arquivos_csv):
    # Verifica se a pasta de saída existe, se não, cria-a
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Inicializa um DataFrame vazio
    combined_df = pd.DataFrame()

    for csv_file in arquivos_csv:
        # Lê cada arquivo CSV em um DataFrame
        df = pd.read_csv(csv_file)
        # Concatena o DataFrame lido com o DataFrame combinado
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Salva o DataFrame combinado como um arquivo CSV na pasta de saída
    combined_df.to_csv(os.path.join(output_folder, 'combined.csv'), index=False)
    print("Arquivos CSV foram unificados com sucesso.")