#Tuplas ()
#Listas [] 
#Dicionarios {} (chave:valor)
#Conjuntos {} (números)

#Exemplo com Tuplas

tupla = ('Goku','Vegeta','Trunks','Gohan')
#Mostrando elementos
print(tupla)
#Alterar Elementos (Não é possivel alterar elementos de uma tupla)
#tupla[0]='Bulma'


#Slicing de elementos(fatiamento)
#Vegeta e Trunks
print(tupla[1:3])

#Trunks e gohan
print(tupla[2:])

#Trunks com indice negativo
print(tupla[-2])

print(len(tupla))  # Tamanho da tupla
print(max(tupla))  # Maior elemento (ordem alfabética)
print(min(tupla))  # Menor elemento (ordem alfabética)
#print(mean(tupla))  # Média (não aplicável para tuplas de strings, mas funciona para tuplas de números)
#print(sum(tupla))  # Soma (não aplicável para tuplas de strings, mas funciona para tuplas de 


#Exemplo com Listas
lista = ['Goku','Vegeta','Trunks','Gohan']
#Mostrando elementos
print(lista)
#Inserir elementos
lista.append('Bulma')
print(lista)
#Inserir elementos em uma posição específica
lista.insert(1,'Kuririn')
print(lista)
#Alterar elementos
lista[0]='Piccolo'
print(lista)
#Remover elementos
lista.remove('Bulma')  # Remove o elemento 'Gohan'
del lista[0]  # Remove o primeiro elemento
print(lista)



#Exemplo com Conjuntos
conjunto = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

# Mostrando elementos
print(conjunto) # Conjuntos não garantem a ordem dos elementos
# Inserir elementos
conjunto.add('Bulma')
print(conjunto)

conjunto.add('Goku')  # Não gera erro se o elemento já existir, mas não o adiciona novamente    


# Remover elementos
conjunto.remove('Goku') # Remove o elemento 'Goku'
conjunto.discard('Trunks') # Remove o elemento 'Trunks' (não gera erro se o elemento não estiver no conjunto)
print(conjunto)

#alterar elementos (não é possível alterar elementos individuais em um conjunto)

#Como descobrir o tipo de algo em python
print(type(conjunto))  # Mostra que é um conjunto

#Update
# pessoa['idade']=45unto))

#Exemplo com Dicionários
#Estrutura de chave: valor
pessoa = {'nome': 'Goku',
            'idade': 43,
            'sexo':'masculino'
        }

#Adicionando elementos
pessoa['raca']= 'sayajin'
pessoa['familia'] = ['Goten', 'Gohan', 'Chi-Chi','Pan']

#Update
pessoa['idade']=45

#Deletando elementos
del pessoa['sexo']  # Remove a chave 'sexo'

#Acessar Chi-Chi
print(pessoa['familia'][2])  # Acessa 'Chi-Chi' na lista de família



# Mostrando elementos
print(pessoa)






