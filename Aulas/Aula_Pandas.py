import pandas as pd
import numpy as np

#Criando labels
indices = ['a', 'b', 'c']
valores = [10, 20, 30]

dic = {'a': 10, 'b': 20, 'c': 30}
dic2 = {'a': 10, 'b': 20, 'd': 40}



series = pd.Series(valores, index=indices)
series2 = pd.Series(dic2)
#print(series)
#print(type(series))
#print(series['a'])

#Operações entre Series

#print(series + series2) #Soma
#print(series - series2) #Subtração
#print(series * series2) #Multiplicação
#print(series / series2) #Divisão

print(series.add(series2, fill_value=0)) #Soma
print(series.sub(series2, fill_value=0)) #Subtração


#Condicionais Pandas

print(series[series > 20]) #Mostra os valores maiores que 15
print(series[series < 15]) #Mostra os valores menores que 15
print(series[series == 10]) #Mostra os valores iguais a 10
print(series[series <= 15]) #Mostra os valores menores ou iguais a 15
print(series[series >= 15]) #Mostra os valores maiores ou iguais a 15

np.random.seed(10)
df = pd.DataFrame(
    index = ['A','B','C','D','E'],
    columns=['W','X','Y','Z'],
    data=np.random.randint(1,50,[5,4])
    )
print(df)


#Fazendo slicing com Iloc(padrão numpy -- indices niméricos)
print(df.iloc[0:2, :]) #Mostra as linhas 0 e 1 e as colunas 1 e 2)

#Fazendo slicing com loc(padrão pandas -- indices alfanuméricos)
print(df.loc['A','B'] ['W','Y']) #Mostra as linhas A, B e C e as colunas W, X e Y)