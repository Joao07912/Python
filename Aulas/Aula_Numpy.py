#Aula sobre numpy
import numpy as np

arr = np.array([10,20,30])

print(arr)
print(type(arr))


#mtz = np.array([10,20,30],[40,50,60])
#print(mtz)

#Funções para estruturar numpy arrays
#Array 1d de 1s

arr=np.ones(10)
print(arr)

#Array 2d de 0s

#mtz= np.zeros(10).reshape(5,2)
mtz= np.zeros([5,2])

print(mtz)

#Arange

arr= np.arange(10,101,10)
print(arr)

#menor valor
print(arr.min())

#maior valor
print(arr.max())

#media 
print(arr.mean())

#indice do maior
print(arr.argmax())
print()
print()
print()
  






#operações com numpy array

arr1 = np.arange(1,10,1)

arr2 = np.arange(9, 0, -1)

print(arr1)
print(arr2)

print(arr1 + arr2)  #soma
print(arr1 - arr2)  #subtração
print(arr1 * arr2)  #multiplicação
print(arr1 / arr2)  #divisão
print(arr1 // arr2) #divisão inteira
print(arr1 % arr2)  #resto da divisão
print(arr1 ** arr2) #potenciação

#concatenação de arrays
print(np.concatenate((arr1, arr2)))



print()
print()
print()
print()
print()
print()

#operações com matrizes
mtz1= np.array([50,10,100,60,25,100,75,80,100]).reshape(3, 3)
print(mtz1)

#somar colunas
print(mtz1.sum(axis=0))  #soma por coluna
#somar linhas   
print(mtz1.sum(axis=1))  #soma por linha
#somar todos os elementos
print(mtz1.sum())  #soma todos os elementos

#somar coluna n
print(mtz1.sum(axis=0)[2])  #soma da terceira coluna

print()
print()
print()

#broadcasting
print(mtz1 / 10)


#números aleatórios com numpy
print(np.random.randint(1,101,10))  #gera 10 números aleatórios entre 1 e 100
#gerar numeros aleatórios iguais entre 2 ou mais dispositivos(exemplo: 10 números iguais)
np.random.seed(10)  #define a semente para gerar números aleatórios
print(np.random.randint(1,101,10))  #gera 10 números aleatórios entre 1 e 100

#números aleatórios e únicos com arrays(unique)
arr = np.random.randint(1,10,10)
print(arr)
print(np.unique(arr))  #retorna os números únicos de um array
#contar a quantidade de vezes que um número aparece em um array
print(np.unique(arr, return_counts=True))  #retorna os números únicos e a quantidade de vezes que aparecem

                                

