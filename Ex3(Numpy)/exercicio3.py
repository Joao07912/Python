import numpy as np

campo = np.zeros((2, 2))
print("Campo minado inicial (2x2):")
print(campo)

print()

linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)
campo[linha, coluna] = 1

print(f"Bomba colocada na posição ({linha}, {coluna})")
print("Campo com bomba:")
print(campo)

print()
print("CAMPO MINADO")
print("Escolha posições de 0 a 1 para linha e coluna")
print()

jogadas = 0
posicoes_jogadas = []
game_over = False

while jogadas < 3 and not game_over:
    print(f"Jogada {jogadas + 1}/3")
    
    try:
        linha = int(input("Digite a linha (0 ou 1): "))
        coluna = int(input("Digite a coluna (0 ou 1): "))
        
        if linha < 0 or linha > 1 or coluna < 0 or coluna > 1:
            print("Posição inválida! Use apenas 0 ou 1")
            continue
            
        if (linha, coluna) in posicoes_jogadas:
            print("Posição já jogada! Tente outra.")
            continue
            
        posicoes_jogadas.append((linha, coluna))
        jogadas += 1
        
        if campo[linha, coluna] == 1:
            print("Game Over! :( Try Again!")
            game_over = True
        else:
            print("Posição segura!")
            
            if len(posicoes_jogadas) == 3: 
                print("Congratulations! You beat the game! :)")
                
    except ValueError:
        print("Digite apenas números!")

print()
print("Campo revelado:")
print(campo)