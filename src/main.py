import csv_files
import menu


status_folder = csv_files.create_csv_files()


if status_folder:
    # global status_files 
    # status_files = csv_files.listar_arquivos_csv()
    menu.menu()

