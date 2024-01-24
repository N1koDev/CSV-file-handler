import pandas as pd

# Função para formatar a data
def formatar_data(data, formato_absoluto):
    # Verifica se o formato é absoluto e retorna a data sem perguntar
    if formato_absoluto:
        return data

    # Verifica se o dia é menor que 12 para determinar o formato
    if int(data[:2]) < 12:
        formato_atual = "DD/MM/YYYY"
        data_formatada = f"{data[4:]}-{data[2:4]}-{data[:2]}"
    else:
        formato_atual = "MM/DD/YYYY"
        data_formatada = f"{data[4:]}-{data[:2]}-{data[2:4]}"

    # Pede confirmação ao usuário apenas se o formato for diferente do absoluto
    if formato_atual != "YYYY-MM-DD":
        confirmacao = input(f"A data {data} está no formato {formato_atual}. Deseja formatar para YYYY-MM-DD? (S/N): ").upper()

        # Verifica a resposta do usuário
        if confirmacao == "S":
            return data_formatada

    return data

# Função para formatar a coluna na planilha
def formatar_coluna_na_planilha(planilha, nome_coluna):
    # Obtém os dados da coluna especificada
    dados_coluna = planilha[nome_coluna].tolist()

    # Usa o formato da primeira data como absoluto
    formato_absoluto = True

    # Lista para armazenar as datas formatadas
    datas_formatadas = []

    # Itera sobre os dados da coluna
    for data_na_coluna in dados_coluna:
        # Chama a função para formatar a data e adiciona à lista
        data_formatada = formatar_data(data_na_coluna, formato_absoluto)
        datas_formatadas.append(data_formatada)

        # Atualiza o formato absoluto se encontrar um diferente
        if formato_absoluto and data_formatada != data_na_coluna:
            formato_absoluto = False

    # Substitui a coluna existente pela coluna formatada
    planilha[nome_coluna] = datas_formatadas

# Função para ler a planilha
def ler_planilha(nome_planilha, nome_coluna):
    try:
        # Lê a planilha
        planilha = pd.read_excel(nome_planilha)

        # Verifica se a coluna especificada existe na planilha
        if nome_coluna not in planilha.columns:
            raise ValueError(f"A coluna {nome_coluna} não foi encontrada na planilha.")

        # Converte a coluna de data para string antes de chamar a função formatar_data
        planilha[nome_coluna] = planilha[nome_coluna].astype(str)

        # Chama a função para formatar a coluna na planilha
        formatar_coluna_na_planilha(planilha, nome_coluna)

        # Salva a planilha com a coluna formatada (substituindo a existente)
        planilha.to_excel(nome_planilha, index=False)
        print(f"A coluna {nome_coluna} foi substituída com as datas formatadas na planilha {nome_planilha}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Solicita ao usuário o nome da planilha e da coluna
nome_planilha = 'date.xlsx'
nome_coluna = 'Data'

# Chama a função para ler a planilha e formatar as datas
ler_planilha(nome_planilha, nome_coluna)
