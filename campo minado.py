def montar_tabuleiro():
    tamanho = int(input("Digite o número de linhas do tabuleiro : "))
    tabuleiro = []
    for i in range(tamanho):
        for j in range(tamanho):
            linha = [""]*tamanho
            tabuleiro.append(linha)
    dimensao = tamanho * tamanho
    print(dimensao)
    for k in range(tamanho):
        print(tabuleiro[k])
    n_minas = 0
    while n_minas == 0:
        n_minas = int(input("Digite a quantidade de minas : "))
        if n_minas > (dimensao/2):
            n_minas = 0
            print(f"Digite um número válido (O número deve ser maior que 0 e menor que {dimensao/2})")
        else:
            if n_minas < 1:
                n_minas = 0
                print(f"Digite um número válido (O número deve ser maior que 0 e menor que {dimensao / 2})")
montar_tabuleiro()