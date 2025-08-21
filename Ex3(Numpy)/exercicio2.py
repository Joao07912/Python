import numpy as np

arr1 = np.arange(0, 52, 2)
print("Números pares de 0 a 51:")
print(arr1)

arr2 = np.arange(100, 49, -2)
print("Números pares de 100 até 50:")
print(arr2)

print()

arr_concatenado = np.concatenate((arr1, arr2))
print("Array concatenado:")
print(arr_concatenado)

print()

arr_ordenado = np.sort(arr_concatenado)
print("Array ordenado:")
print(arr_ordenado)