import csv_files
import convert_to_utf8
import unify_csv_files
import standardize_dates
import replace_delimiters

input_folder = csv_files.input_folder
output_folder = csv_files.output_folder

arquivos_csv = csv_files.arquivos_csv

arquivos = csv_files.listar_arquivos_csv()


def menu():
    while True:
        print(arquivos)

        print("[ 1 ] Converter codificação de caracteres (encoding) para UTF-8")
        print("[ 2 ] Unificar arquivos (limit 999999 linhas por arquivo)")
        print("[ 3 ] Substituir vírgula ',' por ponto e vírgula ';'")
        print("[ 4 ] Substituir ponto e vírgula ';' por vírgula ','")
        print("[ 5 ] Corrigir data para formato YYYY-MM-DD")
        print("[ 0 ] Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            convert_to_utf8.convert_to_utf8(arquivos_csv)
        elif escolha == '2':
            unify_csv_files.unificar_csv(input_folder, output_folder, arquivos_csv)
        elif escolha == '3':
            print("Em andamento")
        elif escolha == '4':
            print("Em andamento")
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