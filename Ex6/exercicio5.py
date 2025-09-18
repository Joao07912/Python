import pandas as pd

ds = pd.read_csv('Datasets/paises.csv', delimiter=';')

def mortalidade(taxa):
    if taxa < 9:
        return 'Balanced'
    else:
        return 'Urgent'

ds['Humanitarian Help'] = ds['Deathrate'].apply(mortalidade)

print("Dataset atualizado:")
print(ds[['Country', 'Deathrate', 'Humanitarian Help']])