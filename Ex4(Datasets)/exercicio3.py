import numpy as np

# Importando o dataset
ds = np.loadtxt('Datasets/space.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

localizacoes = ds[1:, 2]

missoes_eua = np.char.find(localizacoes, 'USA') >= 0
total_missoes_eua = np.sum(missoes_eua)

print(f"Missões realizadas pelos Estados Unidos (EUA): {total_missoes_eua}")