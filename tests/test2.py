import chardet
import codecs
import shutil
import csv_files
import os

arquivos = csv_files.lista_caminho_dos_csv()

# Função para analisar o encoding atual de um arquivo CSV
def analisar_encoding(arquivo):
    resultado = chardet.detect(open(arquivo, 'rb').read())
    encoding = resultado['encoding']
    return encoding

# Função para converter um arquivo CSV para UTF-8
def converter_para_utf8(arquivo, encoding_anterior):
    arquivo_temporario = arquivo + '_temp'
    with codecs.open(arquivo, 'r', encoding=encoding_anterior) as arquivo_origem, \
        open(arquivo_temporario, 'wb') as arquivo_destino:
        for linha in arquivo_origem:
            arquivo_destino.write(linha.encode('utf-8'))
    shutil.move(arquivo_temporario, arquivo)
    return True

# Função para determinar se a conversão é necessária para uma lista de arquivos
def conversao_necessaria_para_lista(arquivos):
    arquivos_necessarios = []
    arquivos_em_utf8 = []
    for arquivo in arquivos:
        encoding_anterior = analisar_encoding(arquivo)
        if encoding_anterior.lower() != 'utf-8':
            arquivos_necessarios.append((arquivo, encoding_anterior))
        else:
            arquivos_em_utf8.append(arquivo)
    return arquivos_necessarios, arquivos_em_utf8
# Exemplo de uso:

arquivos_para_converter, arquivos_em_utf8 = conversao_necessaria_para_lista(arquivos)

if not arquivos_para_converter and arquivos_em_utf8:
    print("Todos os arquivos já estão em UTF-8, a conversão não é necessária.")
else:
    if arquivos_em_utf8:
        # print("Os seguintes arquivos já estão em UTF-8:")
        for arquivo in arquivos_em_utf8:
            nome_arquivo = os.path.basename(arquivo)
            print(f"\nArquivo: {nome_arquivo}")
            print("Enconding anterior: utf-8")
            print("Não necessária a condificação")

    if arquivos_para_converter:
        for arquivo, encoding_anterior in arquivos_para_converter:
            nome_arquivo = os.path.basename(arquivo)
            print(f"\nArquivo: {nome_arquivo}")
            print(f"Encoding anterior: {encoding_anterior}")
            print("Encoding após a conversão: utf-8")
            # Chame a função converter_para_utf8 para fazer a conversão
            converter_para_utf8(arquivo, encoding_anterior)
