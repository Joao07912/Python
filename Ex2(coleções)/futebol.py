times = ['Flamengo', 'Palmeiras', 'São Paulo', 'Internacional', 'Barcelona']

# a. Apenas os 3 primeiros colocados
print('Os 3 primeiros colocados:', times[:3])

# b. Os últimos 2 colocados
print('Os últimos 2 colocados:', times[-2:])

# c. Uma lista com os times em ordem alfabética
print('Times em ordem alfabética:', sorted(times))

# d. Em que posição da tabela se encontra o Barcelona
print('Barcelona está na posição:', (times.index('Barcelona') + 1))