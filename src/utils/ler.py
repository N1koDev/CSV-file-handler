import pandas as pd

def ler_planilha_xlsx(caminho_arquivo):
    try:
        # Use o método read_excel para ler o arquivo xlsx
        dados = pd.read_excel(caminho_arquivo)

        # Exiba os dados (opcional)
        print("Conteúdo da planilha:")
        print(dados)

        # Retorne os dados se desejar usá-los em outro lugar
        return dados

    except Exception as e:
        print(f"Ocorreu um erro ao ler a planilha: {e}")
        return None

# Substitua 'caminho_do_arquivo.xlsx' pelo caminho real do seu arquivo
caminho_do_arquivo = 'cnpjs.xlsx'
ler_planilha_xlsx(caminho_do_arquivo)
