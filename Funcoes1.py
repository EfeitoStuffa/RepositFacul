#1.	Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

def Idade_em_dias():
    idade_anos = int(input("Digite quantos anos você tem : "))
    idade_dias = idade_anos * 365
    print(f"Você tem {idade_dias} dias de vida. Congratulações!")
Idade_em_dias()