#funcao exibir numeros entre "a" e "b" sendo "a" e "b" parametros da funcao

def exibir_numeros(num_1,num_2):
    if num_1 > num_2:
        exibir_numeros(num_1-1,num_2)
        print(num_1)
    if num_2 > num_1:
        exibir_numeros(num_1,num_2-1)
        print(num_2)


num_1 = int(input("Digite o primeiro numero :"))
num_2 = int(input("Digite o primeiro numero :"))

exibir_numeros(num_1,num_2)