import pandas as pd

def formatar_hora(numero):
    # Verifica se o número já está no formato correto
    if ':' in numero:
        return numero

    # Adiciona zeros à esquerda se o número for curto
    numero = numero.rjust(6, '0')

    # Formata o número como HH:MM:SS
    hora_formatada = f'{numero[:2]}:{numero[2:4]}:{numero[4:]}'
    return hora_formatada

def main():
    # Substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo Excel
    arquivo_excel = 'time.xlsx'

    try:
        # Carrega o arquivo Excel
        df = pd.read_excel(arquivo_excel)

        # Nome da coluna que contém os números
        coluna_numeros = 'HOUR'

        # Itera sobre cada célula da coluna e formata como hora
        for indice, valor in df[coluna_numeros].items():
            try:
                # Formata o número como hora, apenas se não estiver no formato correto
                hora_formatada = formatar_hora(str(valor))
                # Converte a coluna para object antes de atribuir os valores formatados
                df[coluna_numeros] = df[coluna_numeros].astype('object')
                # Atualiza o DataFrame com a hora formatada
                df.at[indice, coluna_numeros] = hora_formatada
            except ValueError:
                print(f"Erro ao formatar hora na linha {indice + 2}: {valor}")

        # Salva o DataFrame de volta no arquivo Excel
        df.to_excel(arquivo_excel, index=False)
        print(f"Horas formatadas e arquivo {arquivo_excel} atualizado com sucesso!")

    except FileNotFoundError:
        print(f"Arquivo {arquivo_excel} não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
