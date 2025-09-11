import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print("DataFrame:")
print(df)
print()


coluna_x_menor_30 = df['X'][df['X'] < 30]
media_x_menor_30 = coluna_x_menor_30.mean()

print("Média dos elementos da coluna X menores que 30:", media_x_menor_30)