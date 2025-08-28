import numpy as np

#Slicing em numpy arrays

#Criando numpy array 2d
mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)

#Slicing

print(mtz[2])  #Terceira linha
print(mtz[:,1])  #Segunda coluna

print(mtz[:,1:]) #Segunda coluna até a última
print(mtz[1:,:]) #Segunda linha até a última

#Condicionais no Numpy array

print(mtz>5)  #Retorna um array booleano com True onde a condição é satisfeita

print(mtz[mtz > 5])  #Elementos maiores que 5
print(mtz[mtz%2 == 0])  #Elementos pares
print(mtz[mtz%2 != 0])  #Elementos ímpares


#Tratamento Textual

arr=np.array(['goku','GOten','Gohan','Trunks','Bulma'])
print(arr)

arr = np.char.upper(arr)  #Transforma todos os elementos em maiúsculo

print(np.char.find(arr,'GO'))  #Retorna o indice onde o caracter 'Go' está [0 0 0 -1 -1]

print(np.char.find(arr,'GO')>=0)  #Retorna um array booleano com True onde o caracter 'Go' está presente [ True  True  True False False]

print(arr[np.char.find(arr,'GO')>=0])  #Retorna os elementos que possuem o caracter 'Go' ['Goku' 'Goten' 'Gohan']





