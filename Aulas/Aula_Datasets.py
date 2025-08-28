import numpy as np

#Importando datasets no numpy

ds=np.loadtxt('Datasets/space.csv',
              delimiter=';',
              dtype='str',
              encoding='utf-8')  
#print(ds)

#Slicing para pegar apenas as colunas

#pegar todas as colunas
print(ds[0,:])

#Calculando a média de uma missao espacial
#Slicing para extrair a coluna custo (Cost)

ds_cost= ds[1:,6]

print(ds_cost)
ds_cost=ds_cost.astype('float')  #Convertendo os valores para float
print(ds_cost.mean()) #Calculando a média dos custos

#remover valores = 0 da coluna custo
ds_cost=ds_cost[ds_cost>0]
print(ds_cost.mean())  #Calculando a média dos custos sem os valores 0


