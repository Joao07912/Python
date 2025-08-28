import numpy as np

# Importando o dataset
ds = np.loadtxt('Datasets/space.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')


# Extraindo a coluna de status das missões (última coluna)
status_missoes = ds[1:, -1]  

# Contando missões bem-sucedidas
missoes_sucesso = np.sum(status_missoes == 'Success')
total_missoes = len(status_missoes)

print(f"Total de missões: {total_missoes}")
print(f"Missões bem-sucedidas: {missoes_sucesso}")

porcentagem_sucesso = (missoes_sucesso / total_missoes) * 100

print(f"Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%")
