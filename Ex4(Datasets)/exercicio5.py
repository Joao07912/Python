import numpy as np

ds = np.loadtxt('Datasets/space.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

# Extraindo a coluna de empresas (coluna 1)
empresas = ds[1:, 1]

empresas_unicas, contagens = np.unique(empresas, return_counts=True)

print("Empresas que já realizaram missões espaciais:")
print()

# Usando for para mostrar as informações
for i in range(len(empresas_unicas)):
    print(f"{empresas_unicas[i]}: {contagens[i]} missões")