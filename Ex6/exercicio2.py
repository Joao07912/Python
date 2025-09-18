import pandas as pd
import numpy as np

ds = pd.read_csv('Datasets/paises.csv', delimiter=';')

maior = np.argmax(ds['Population'])

nome = ds.iloc[maior]['Country']
regiao = ds.iloc[maior]['Region']

print("País com maior população: ", nome)
print("Região: ", regiao)