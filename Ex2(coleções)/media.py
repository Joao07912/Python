aluno = {}
aluno['nome'] = input('Digite o seu nome: ')
aluno['media'] = float(input('Digite a sua média: '))

# Determinando a situação do aluno
if aluno['media'] >= 50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

# Exibindo os dados do aluno
print(aluno['nome'], 'tem média', aluno['media'], 'e está em situação', aluno['situacao'])


    