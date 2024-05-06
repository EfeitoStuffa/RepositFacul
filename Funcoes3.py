# 3. Faça uma função que recebe por parâmetro o raio de uma esfera e calcule o seu volume (v = (4 x pi x R3)/3).

def Calcular_volume_esfera():
    raio_esfera = float(input("Digite o raio_esfera da esfera : "))
    while raio_esfera < 0 :
        raio_esfera = float(input("Digite o raio_esfera da esfera : "))
    volume_esfera = ((4 * 3.14 * raio_esfera * raio_esfera * raio_esfera)/3)
    print(f"O volume de sua esfera, com raio_esfera {raio_esfera}, é : {volume_esfera:.2f}")
Calcular_volume_esfera()