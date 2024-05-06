# 2. Faça uma função que recebe a média final de um aluno por parâmetro e
# retorna o seu conceito, conforme a tabela abaixo:
# Nota 	Conceito
# De 0 a 49 	D
# De 50 a 69 	C
# De 70 a 89 	B
# De 90 a 100 	A

def Media_Final():
    media_final = int(input("Digite sua média final : "))
    if 0 < media_final < 49 :
        conceito = "D"
        parabains = "Dá para miorah neh"
    else:
        if 50 < media_final < 69:
            conceito = "C"
            parabains = "Dá para miorah neh"
        else:
            if 70 < media_final < 89:
                conceito = "B"
                parabains = "Congratulações rapah!"
            else:
                if 90 < media_final < 100:
                    conceito = "A"
                    parabains = "Congratulações rapah!"
                else:
                    print("Média final inválida.")
    print(f"Conforme sua média final de {media_final}, seu conceito é {conceito} . {parabains}")
Media_Final()