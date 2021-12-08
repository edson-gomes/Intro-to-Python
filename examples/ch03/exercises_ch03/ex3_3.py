# (O que este código faz?) O que o programa a seguir imprime?

for linha in range(10):
    for coluna in range(10):
        print('<' if linha % 2 == 1 else '>', end='')
    print()

# O programa imprime um quadrado de tamanho 10 x 10 caracteres em que, nas linhas pares, a linha é preenchida com 10 caracteres > e, nas linhas ímpares, a linha é preenchida com 10 caracteres <. Isso assumindo-se que a primeira linha é contada como linha 0.
