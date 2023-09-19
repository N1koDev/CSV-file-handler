import chardet
import codecs
import shutil
import os

# Função para analisar o encoding atual de um arquivo CSV
def analisar_encoding(arquivo):
    resultado = chardet.detect(open(arquivo, 'rb').read())
    encoding = resultado['encoding']
    return encoding

# Função para converter um arquivo CSV para UTF-8-SIG
def converter_para_utf8_sig(arquivo, encoding_anterior):
    arquivo_temporario = arquivo + '_temp'
    try:
        with codecs.open(arquivo, 'r', encoding=encoding_anterior) as arquivo_origem, \
            open(arquivo_temporario, 'wb') as arquivo_destino:
            for linha in arquivo_origem:
                arquivo_destino.write(linha.encode('utf-8-sig'))  # Alterado para utf-8-sig
        # Realize a cópia do arquivo temporário para backup, caso a conversão seja bem-sucedida
        shutil.copyfile(arquivo, arquivo + '_backup')
        # Mova o arquivo temporário para substituir o arquivo original
        shutil.move(arquivo_temporario, arquivo)
        return True
    except Exception as e:
        print(f"Erro ao converter {arquivo}: {str(e)}")
        return False

# Função para determinar se a conversão é necessária para uma lista de arquivos
def conversao_necessaria_para_lista(arquivos):
    arquivos_necessarios = []
    arquivos_em_utf8 = []
    for arquivo in arquivos:
        encoding_anterior = analisar_encoding(arquivo)
        if encoding_anterior.lower() != 'utf-8-sig':  # Alterado para utf-8-sig
            arquivos_necessarios.append((arquivo, encoding_anterior))
        else:
            arquivos_em_utf8.append(arquivo)
    return arquivos_necessarios, arquivos_em_utf8

# Exemplo de uso:

def convert_to_utf8_sig(arquivos):
    arquivos_para_converter, arquivos_em_utf8 = conversao_necessaria_para_lista(arquivos)

    if not arquivos_para_converter and arquivos_em_utf8:
        print("Todos os arquivos já estão em UTF-8-SIG, a conversão não é necessária.")
    else:
        if arquivos_em_utf8:
            for arquivo in arquivos_em_utf8:
                nome_arquivo = os.path.basename(arquivo)
                print(f"\nArquivo: {nome_arquivo}")
                print("Encoding anterior: utf-8-sig")
                print("Não necessária a conversão")

        if arquivos_para_converter:
            for arquivo, encoding_anterior in arquivos_para_converter:
                nome_arquivo = os.path.basename(arquivo)
                print(f"\nArquivo: {nome_arquivo}")
                print(f"Encoding anterior: {encoding_anterior}")
                print("Encoding após a conversão: utf-8-sig")
                if converter_para_utf8_sig(arquivo, encoding_anterior):
                    print(f"Conversão bem-sucedida para {arquivo}")
                else:
                    print(f"Conversão falhou para {arquivo}")