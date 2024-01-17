import csv_files
import convert_to_utf8
import convert_to_utf8sig
import unify_csv_files
import standardize_dates
import convert_xlsx_to_csv

input_folder = csv_files.input_folder
output_folder = csv_files.output_folder
arquivos_csv = csv_files.arquivos_csv
arquivos_xlsx = csv_files.arquivos_xlsx

def menu():
    csv_files.create_folders()
    while True:
        print("Arquivos disponíveis (CSV):")
        for idx, arquivo in enumerate(arquivos_csv):
            print(f"{idx + 1}. {arquivo}")

        print("\nArquivos disponíveis (XLSX):")
        for idx, arquivo_xlsx in enumerate(arquivos_xlsx):
            print(f"{idx + 1}. {arquivo_xlsx}")

        print("\n[ 1 ] Converter codificação de caracteres (encoding) para UTF-8")
        print("[ 2 ] Unificar arquivos (limit 999999 linhas por arquivo)")
        print("[ 3 ] Substituir vírgula ',' por ponto e vírgula ';'")
        print("[ 4 ] Substituir ponto e vírgula ';' por vírgula ','")
        print("[ 5 ] Corrigir data para formato YYYY-MM-DD")
        print("[ 6 ] Converter XLSX para CSV")
        print("[ 0 ] Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            convert_to_utf8sig.convert_to_utf8_sig(arquivos_csv)
        elif escolha == '2':
            unify_csv_files.unify_csv_files(input_folder, output_folder, arquivos_csv)
        elif escolha == '3':
            # Implemente a lógica para substituir vírgula por ponto e vírgula
            pass
        elif escolha == '4':
            # Implemente a lógica para substituir ponto e vírgula por vírgula
            pass
        elif escolha == '5':
            standardize_dates.standardize_dates(arquivos_csv)
        elif escolha == '6':
            convert_xlsx_to_csv.convert_xlsx_to_csv(input_folder, output_folder)
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        continuar = input("Deseja continuar? (S/N): ")
        if continuar.upper() != 'S':
            print("Saindo do programa.")
            break

menu()
