import detectar_encoding

def detectar_delimitador(arquivo_csv):
    encoding = detectar_encoding.detectar_encoding(arquivo_csv)

    # Tenta detectar automaticamente o delimitador olhando para as primeiras 2 linhas do arquivo.
    with open(arquivo_csv, 'r', encoding=encoding) as file:
        primeira_linha = file.readline()
        segunda_linha = file.readline()

    # Lista de delimitadores a serem verificados
    delimitadores = [';', ',', '\t', '|']  # Adicione outros delimitadores, se necessário

    for delimitador in delimitadores:
        if primeira_linha.count(delimitador) > 1 or segunda_linha.count(delimitador) > 1:
            return delimitador

    # Se não foi possível detectar automaticamente, você pode especificar o delimitador manualmente.
    return ','  # Substitua pelo delimitador correto se necessário.