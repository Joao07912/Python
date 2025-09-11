import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
)

print("DataFrame original:")
print(df)
print()


slicing_df = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print("Slicing (linhas A, C, E e colunas X, Y):")
print(slicing_df)
print()

soma_linhas = slicing_df.sum(axis=1)
print("Soma dos elementos de cada linha:")
print(soma_linhas)
print()

soma_colunas = slicing_df.sum(axis=0)
print("Soma dos elementos de cada coluna:")
print(soma_colunas)