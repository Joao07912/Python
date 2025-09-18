import pandas as pd
import numpy as np

#Importação de datasets no pandas

ds = pd.read_csv('Datasets/paises.csv', delimiter=';')
#print(ds.columns) #Mostra as colunas
#print(ds.head(5)) #Mostrando as 5 primeiras linhas
#print(ds.tail(5)) #Mostrando as 5 ultimas linhas

#Criar uma nova coluna que mostre a porcentaem da populção de cada pais em relação a população global
somaPopulacao = np.sum(ds['Population'])
#print(somaPopulacao)


#porcentagem = (populacaoPais / somaPopulacao) * 100
populationPerc = (ds['Population'] / somaPopulacao) * 100
#print(populationPerc)

#Adicionar nova coluna no dataset
ds[populationPerc]=populationPerc
#print(ds)

#Criando uma nova versão do dataset
ds.to_csv('Datasets/paises2.csv', sep=';')

#Agrupamento de dados
#Agrupar os dados do dataset por região

group_region = ds.groupby('Region')
#print(group_region.count()['Country'])

#print(group_region.sum()['Country'])


print(group_region.sum()['Population'])

#Funções customizadas no pandas

#Criando uma função que da um desconto de 10% em algo
def tenpercent(x):
    return x * 0.9


#pegando a taxa de mortalidade do dataset
taxaMort = ds['Deathrate']

#Criando uma nova series descontando 10% da taxa de mortalidade

taxaMort2 = taxaMort.apply(tenpercent)


#Criando um novo dataframe apenas com essas duas series
df2 = pd.concat([taxaMort, taxaMort2], axis=1)
df2.columns = ['Taxa de Mortalidade', 'Taxa de Mortalidade com Desconto']
print(df2)


#Removendo linhas que possuam dados ausentes usando dropna()
df2 = df2.dropna()

#Preenchendo dados ausentes com um valor específico
df2 = df2.fillna(0)



