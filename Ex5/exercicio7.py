import pandas as pd
import numpy as np

# Criando o DataFrame exemplo do tópico 5.3
np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print("DataFrame:")
print(df)
print()


media_linha_d = df.loc['D'].mean()
soma_linha_e = df.iloc[4].sum()

print("Média dos elementos da linha D (usando loc):",media_linha_d)
print("Soma dos elementos da linha E (usando iloc):",soma_linha_e)