#funcao exibir numeros impares 1 a 30

def exibir_impares(numero):
    if numero > 1:
        exibir_impares(numero-1)
    if numero % 2 == 0:
        print(numero)
    



exibir_impares(30)