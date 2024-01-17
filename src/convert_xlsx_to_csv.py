import pandas as pd
import os
import csv_files

def convert_xlsx_to_csv(input_folder, output_folder):
    arquivos_xlsx = csv_files.arquivos_xlsx

    if not arquivos_xlsx:
        print("Não há arquivos XLSX na pasta de entrada.")
        return

    for idx, xlsx_file in enumerate(arquivos_xlsx):
        try:
            df = pd.read_excel(xlsx_file)

            # Escolha da codificação
            utf_option = input(f"Deseja que o CSV {os.path.basename(xlsx_file)} seja em UTF-8? (S/N): ")
            encoding_option = 'utf-8' if utf_option.upper() == 'S' else 'utf-8-sig'

            # Escolha do separador
            separator_option = input("Escolha o separador desejado (',' para vírgula, '.' para ponto, ';' para ponto e vírgula): ")
            if separator_option == ',':
                sep_option = ','
            elif separator_option == '.':
                sep_option = '.'
            elif separator_option == ';':
                sep_option = ';'
            else:
                print("Opção inválida. Usando vírgula como separador.")
                sep_option = ','

            base_name = os.path.splitext(os.path.basename(xlsx_file))[0]
            csv_file = os.path.join(output_folder, f"{base_name}.csv")
            df.to_csv(csv_file, index=False, encoding=encoding_option, sep=sep_option)
            print(f"Conversão do arquivo {base_name}.xlsx concluída. Arquivo CSV salvo em {csv_file}")
        except Exception as e:
            print(f"Erro ao converter {base_name}.xlsx para CSV: {e}")

if __name__ == "__main__":
    convert_xlsx_to_csv(csv_files.input_folder, csv_files.output_folder)
