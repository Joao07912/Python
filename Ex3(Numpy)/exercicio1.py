import numpy as np

arr1 = np.ones(8)
print("Array de 1's:")
print(arr1)

arr2 = np.random.randint(0, 10, 8)
print("Array de números aleatórios (0-9):")
print(arr2)

arr_resultado = arr1 + arr2
print("Array resultante da soma:")
print(arr_resultado)

soma_total = arr_resultado.sum()
print("Soma de todos os elementos:", soma_total)

print()

if soma_total >= 40:
    matriz_final = arr_resultado.reshape(4, 2)
    print("Soma >= 40: Remodelando para mais linhas que colunas (4x2)")
else:
    matriz_final = arr_resultado.reshape(2, 4)
    print("Soma < 40: Remodelando para mais colunas que linhas (2x4)")

print("Matriz final:")
print(matriz_final)