import numpy as np

ds = np.loadtxt('Datasets/paises.csv',
                delimiter=';',
                dtype='str',
                encoding='utf-8')

print(ds[:, 0:4]) #Mostra os 4 primeiros campos da tabela 

quant = np.unique(ds[1:, 1])
print(len(quant)) 
print(np.unique(ds[1:, 1])) #Mostra as diferentes regiões do dataset


ds_literacy = ds[1:, 9].astype('float') # Extraindo a coluna de alfabetização
  # Convertendo para float
media_alfabetizacao = np.mean(ds_literacy)  # Calculando a média
print(media_alfabetizacao)


regioes = ds[1:, 1]  # Extraindo a coluna de regiões
america_norte = np.char.find(regioes, 'NORTHERN AMERICA') >=0
print(np.sum(america_norte))


america_Sul_Caribe = np.char.find(regioes, 'LATIN AMER. & CARIB') >=0

ds_gpd = ds[1:, 8].astype('float')
mais_rico = np.argmax(ds_gpd[america_Sul_Caribe])
print(ds[1:, 0][america_Sul_Caribe][mais_rico])





















