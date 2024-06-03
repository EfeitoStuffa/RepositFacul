#funcao recursiva 1 a 10
def exibir_numeros(numero):
    if numero > 1:
        exibir_numeros(numero-1)
    print(numero)


exibir_numeros(10)