import numpy as np

matriz = np.random.randint(1, 30, (3, 5))
print("Matriz criada:")
print(matriz)

print()

linhas, colunas = matriz.shape

print(f"Número de linhas: {linhas}")
print(f"Número de colunas: {colunas}")

total = linhas * colunas
print(f"Total de elementos: {total}")

print()

if total % 2 == 0:
    print(f"Esta matriz poderia se tornar um vetor unidimensional com número PAR de elementos ({total})")
else:
    print(f"Esta matriz poderia se tornar um vetor unidimensional com número ÍMPAR de elementos ({total})")

