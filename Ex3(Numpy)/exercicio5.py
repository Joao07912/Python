import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))
print("Matriz 4x4:")
print(matriz)

print()
print()

print("MÉDIAS")
medias_linhas = matriz.mean(axis=1)
medias_colunas = matriz.mean(axis=0)

print("Média de cada linha:")
for i, media in enumerate(medias_linhas):
    print(f"Linha {i+1}: {media:.2f}")

print()
print("Média de cada coluna:")
for i, media in enumerate(medias_colunas):
    print(f"Coluna {i+1}: {media:.2f}")

print()
print()

print("MAIORES MÉDIAS")
mm_linhas= medias_linhas.max()
mm_colunas = medias_colunas.max()

print(f"Maior média das linhas: {mm_linhas:.2f}")
print(f"Maior média das colunas: {mm_colunas:.2f}")

print()
print()

print("ANÁLISE DE FREQUÊNCIA")
numeros_unicos, contagens = np.unique(matriz, return_counts=True)

print("Quantidade de aparições de cada número:")
for numero, contagem in zip(numeros_unicos, contagens):
    print(f"Número {numero}: {contagem} vezes")

print()
print("Números que aparecem  2 vezes:")
numeros_duas_vezes = numeros_unicos[contagens == 2]
if len(numeros_duas_vezes) > 0:
    print(numeros_duas_vezes)
else:
    print("Nenhum número aparece exatamente 2 vezes")