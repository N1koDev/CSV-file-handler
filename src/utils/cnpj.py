import pandas as pd

def formatar_cnpj(numero):
    # Remove qualquer caractere não numérico do número do CNPJ
    numero = ''.join(filter(str.isdigit, numero))

    # Adiciona zeros à esquerda se o número do CNPJ for curto
    numero = numero.rjust(14, '0')

    # Verifica se o CNPJ já está no formato padrão
    if (
        numero[2] == '.' and numero[6] == '.' and
        numero[10] == '/' and numero[15] == '-'
    ):
        return numero  # Mantém o formato padrão

    # Formata o número como CNPJ
    cnpj_formatado = f'{numero[:2]}.{numero[2:5]}.{numero[5:8]}/{numero[8:12]}-{numero[12:]}'
    return cnpj_formatado

def main():
    # Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
    arquivo_excel = 'cnpjs.xlsx'

    try:
        # Carrega o arquivo Excel
        df = pd.read_excel(arquivo_excel)

        # Nome da coluna que contém os números
        coluna_numeros = 'CNPJS'

        # Aplica a formatação de CNPJ apenas aos que não estão no formato padrão
        df[coluna_numeros] = df[coluna_numeros].astype(str).apply(formatar_cnpj)

        # Salva o DataFrame de volta no arquivo Excel
        df.to_excel(arquivo_excel, index=False)
        print(f"CNJPs formatados e arquivo {arquivo_excel} atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {arquivo_excel} não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
