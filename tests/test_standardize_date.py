import pandas as pd
from dateutil import parser

# Criar um DataFrame de exemplo
data = {'Data/Hora': ['29/08/2023 06:08:50']}
df = pd.DataFrame(data)

# Função para obter o formato identificado pelo dateutil
def identify_date_format(date_string):
    try:
        parsed_date = parser.parse(date_string)
        return parsed_date
    except ValueError:
        return None  # Retornar None se não puder ser analisado como data/hora

# Aplicar a função para identificar o formato da data/hora e converter para objeto de data/hora
df['Data/Hora'] = df['Data/Hora'].apply(identify_date_format)

# Dividir a coluna 'Data/Hora' em 'Data' e 'Hora'
df['Data'] = df['Data/Hora'].dt.strftime('%Y-%m-%d')
df['Hora'] = df['Data/Hora'].dt.strftime('%H:%M:%S')

# Exibir o DataFrame resultante
print(df[['Data', 'Hora']])
