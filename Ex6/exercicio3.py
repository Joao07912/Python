import pandas as pd


ds = pd.read_csv('Datasets/paises.csv', delimiter=';')

group_region = ds.groupby('Region')

alfa_media = group_region['Literacy (%)'].mean()

print("Média de alfabetização por região:")
print(alfa_media)