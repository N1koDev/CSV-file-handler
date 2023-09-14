import chardet

# Função para detectar o encoding correto de um arquivo CSV
def detectar_encoding(arquivo_csv):
    # Detecta o encoding usando a biblioteca chardet
    with open(arquivo_csv, 'rb') as f:
        resultado = chardet.detect(f.read())
    
    # Retorna o encoding detectado
    return resultado['encoding']