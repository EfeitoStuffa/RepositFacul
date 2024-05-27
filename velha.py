velha = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

game_over = False
n_jogadas_x = 0
n_jogadas_o = 0
turnos = 0
v_x = False
v_o = False
while game_over == False:
    for i in range(3):
        print(velha[i])
    turnos = turnos + 1
    jogada_x = int(input("Digite sua jogada : "))
    while n_jogadas_x < turnos:
        for j in range(len(velha)):
            for k in range(len(velha[i])):
                if velha[j][k] == jogada_x:
                    velha[j][k] = 'X'
                    n_jogadas_x = n_jogadas_x + 1
        if n_jogadas_x < turnos:
            jogada_x = int(input("Digite uma posição válida : "))
    for i in range(3):
        print(velha[i])
    jogada_o = int(input("Digite sua jogada : "))
    while n_jogadas_o < turnos:
        for j in range(len(velha)):
            for k in range(len(velha[i])):
                if velha[j][k] == jogada_o:
                    velha[j][k] = 'O'
                    n_jogadas_o = n_jogadas_o + 1
        if n_jogadas_o < turnos:
            jogada_o = int(input("Digite uma posição válida : "))



    #Testando Condições de Vitória
    cnt = 0
    for l in range(len(velha)):
        for m in range(len(velha)):
            if velha[l] == ['X','X','X'] :
                game_over = True
                v_x = True
            else:
                if velha[l][m] == 'X':
                    cnt = cnt + 1
                    if cnt == 3:
                        game_over = True
                        v_x = True



















#                else:
#                    if velha[i] == ['O','O','O'] :
#                        game_over = True
#                        v_o = True
#                    else:
#                        if velha[j] == ['O', 'O', 'O']:
#                            game_over = True
#                            v_o = True