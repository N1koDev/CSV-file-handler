import codecs
import csv
import csv_files

arquivos = csv_files.lista_caminho_dos_csv()

def is_utf8_encoded(file_path):
    try:
        with codecs.open(file_path, 'r', encoding='utf-8') as file:
            csv.reader(file)
        return True
    except UnicodeDecodeError:
        return False

for arquivo in arquivos:
    if is_utf8_encoded(arquivo):
        print(f'O arquivo "{arquivo}" está codificado em UTF-8.')
    else:
        print(f'O arquivo "{arquivo}" não está codificado em UTF-8.')
