

nome = input('Digite seu nome completo: ')

print('Nome em maiúsculas:', nome.upper())
print('Nome em minúsculas:', nome.lower())
print('Quantidade de letras:', len(nome.replace(' ', '')))
partes = nome.split()
partes[-1] = 'do Inatel'
print('Nome com sobrenome trocado:', ' '.join(partes))

print('\n'+'\n')



numero = int(input('Digite o número para ver a tabuada: '))
inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

for i in range(inicio, fim + 1):
    print('{} x {} = {}'.format(numero, i, numero * i))

print('\n' + '\n')



sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo [M/F]: ').upper()
    if sexo == 'M':
        print('Você é homem.')
    elif sexo == 'F':
        print('Você é mulher.')
    else:
        print('Sexo inválido. Tente novamente.')

print('\n'+'\n')



distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('O preço da passagem será de R${:.2f}'.format(preco))

print('\n' +'\n')



while True:
    numero = int(input('Digite um número entre 1000 e 9999: '))
    if 1000 <= numero <= 9999:
        break
    else:
        print('Número inválido! Tente novamente.')

unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = numero // 1000

print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)

print('\n' + '\n')


import math

num = float(input('Digite um número decimal: '))

print('Raiz quadrada:', math.sqrt(num))
print('Teto:', math.ceil(num))
print('Chão:', math.floor(num))
print('Parte inteira:', math.trunc(num))
