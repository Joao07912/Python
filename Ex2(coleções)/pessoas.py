n = int(input("Quantas pessoas você deseja cadastrar? "))
pessoas = {}

# Loop para ler os dados de cada pessoa
for i in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    pessoas[i] = {'nome': nome, 'idade': idade, 'sexo': sexo}

# Calcular a média de idade
soma = sum(p['idade'] for p in pessoas.values())
media = soma / (len(pessoas))
print("A média de idade das pessoas cadastradas é:", media)

# Contar quantas mulheres têm menos de 20 anos
m_20 = 0  
for p in pessoas.values():
    if p['sexo'] == 'F' and p['idade'] < 20:
        m_20 += 1
print("A quantidade de mulheres com menos de 20 anos é:", m_20)


