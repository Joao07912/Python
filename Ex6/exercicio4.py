import pandas as pd


ds = pd.read_csv('Datasets/paises.csv', delimiter=';')

sem_costa = ds[ds['Coastline (coast/area ratio)'] == 0]

sem_costa.to_csv('noCoast.csv', sep=';', index=False)

print("Países sem costa marítima:")
print(sem_costa['Country'])
