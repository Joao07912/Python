import pandas as pd


ds = pd.read_csv('Datasets/paises.csv', delimiter=';')

oceania = ds[ds['Region'].str.contains('OCEANIA', na=False)]
print("Países da Oceania:")
print(oceania['Country'])
