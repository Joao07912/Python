import numpy as np

ds = np.loadtxt('Datasets/space.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

# Extraindo a coluna de custos (coluna 6)
custos_str = ds[1:, 6]

custos = custos_str.astype('float')

# Filtrando apenas valores > 0
custos_validos = custos[custos > 0]

media_custos = custos_validos.mean()

print(f"Média de gastos de uma missão espacial: ${media_custos:.2f} milhões")