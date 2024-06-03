#Corrigir a VERTICAL
def Verificar_vencedor(jogador,velha, game_over):
    for o in range (len(jogador)):
        cnt_diagonal_1 = 0
        cnt_diagonal_2 = 0
        cnt_vertical = [0, 0, 0]
        for l in range(len(velha)):
            if velha[l] == [jogador[o], jogador[o], jogador[o]]:
                game_over = True
                vitoria[o] = True
                print(f"Vitória horizontal na linha {l} de {jogador[o]}")
            if velha[l][l] == jogador[o]:
                cnt_diagonal_1 = cnt_diagonal_1 + 1
                if cnt_diagonal_1 == 3:
                    game_over = True
                    vitoria[o] = True
                    print(f"Vitória na diagonal primaria de {jogador[o]}")
            if velha[l][len(velha)-l-1] == jogador[o]:
                cnt_diagonal_2 = cnt_diagonal_2 + 1
                if cnt_diagonal_2 == 3:
                    game_over = True
                    vitoria[o] = True
                    print(f"Vitória na diagonal secundária de {jogador[o]}")
            #cnt_vertical = 0
            #vertical = 0
            for m in range(len(velha)):
                if velha[m][l] == jogador[o]:
                    cnt_vertical[l] = cnt_vertical[l] + 1
                    if cnt_vertical[l] == 3:
                        game_over = True
                        vitoria[o] = True
                        print(f"Vitória na vertical {m} de {jogador[o]}")
                #vertical = vertical + 1
    return True

velha = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
    ]
velha_visual = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

game_over = False
n_jogadas_x = 0
n_jogadas_o = 0
num_jogadas = [0,0]
turnos = 0
vitoria = [False, False]
jogador = ['X', 'O']
print("Jogo da Velha")
while game_over == False:
    turnos = turnos + 1
    if turnos != 1:
        print()
        print()
        print()
        print()
        print()
        print()
    print(f"Começo da rodada {turnos}")
    for i in range(3):
        print(velha_visual[i])
    for n in range (len(jogador)):
        if num_jogadas[0] == 5:
            print("Velha!")
            game_over = True
        else:
            if game_over == False :
                jogada = str(input(f"Jogador {n+1}, digite sua jogada : "))
                while num_jogadas[n] < turnos:
                    for j in range(len(velha)):
                        for k in range(len(velha[j])):
                            if velha[j][k] == jogada:
                                velha_visual[j][k] = jogador[n]
                                velha[j][k] = jogador[n]
                                num_jogadas[n] = num_jogadas[n] + 1
                    if num_jogadas[n] < turnos:
                        jogada = str(input("Digite uma posição válida : "))
                print()
                print()
                print()
                print()
                print()
                print()
                for i in range(3):
                    print(velha_visual[i])
            Verificar_vencedor(jogador, velha, game_over)
#    jogada_o = int(input("Digite sua jogada : "))
#    while n_jogadas_o < turnos:
#        for j in range(len(velha)):
#            for k in range(len(velha[i])):
#                if velha[j][k] == jogada_o:
#                    velha[j][k] = 'O'
#                    n_jogadas_o = n_jogadas_o + 1
#        if n_jogadas_o < turnos:
#            jogada_o = int(input("Digite uma posição válida : "))



    #Testando Condições de Vitória
    #cnt_vertical = 0
