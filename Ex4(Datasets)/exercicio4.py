import numpy as np

ds = np.loadtxt('Datasets/space.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

# Extraindo colunas necessárias
empresas = ds[1:, 1]  # Company Name
custos_str = ds[1:, 6]  # Cost
detalhes = ds[1:, 4]  # Detail (nome da missão)

# Filtrando missões da SpaceX
missoes_spacex = np.char.find(empresas, 'SpaceX') >= 0

custos_spacex_str = custos_str[missoes_spacex]
detalhes_spacex = detalhes[missoes_spacex]

custos_spacex = custos_spacex_str.astype('float')

# Encontrando a missão mais cara
indice_mais_cara = np.argmax(custos_spacex)
custo_mais_caro = custos_spacex[indice_mais_cara]
missao_mais_cara = detalhes_spacex[indice_mais_cara]

print(f"Missão mais cara da SpaceX: {missao_mais_cara}")
print(f"Custo: ${custo_mais_caro:.2f} milhões")