matriz = [[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],
[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]
def somar_diagonais_primaria_secundaria(matriz):
    soma_diagonal_primaria = 0
    soma_diagonal_secundaria = 0
    soma_diagonais = 0
    tamanho_matriz = len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j :
                soma_diagonal_primaria = soma_diagonal_primaria + matriz[i][j]
            else:
                if (j + 1) == (len(matriz) - i):
                    soma_diagonal_secundaria = soma_diagonal_secundaria + matriz[i][j]
    soma_diagonais = soma_diagonal_primaria + soma_diagonal_secundaria
    return soma_diagonais

print(somar_diagonais_primaria_secundaria(matriz))