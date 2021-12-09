"""(Separando os dígitos em um inteiro) No exercício 2.11, você escreveu um script para separar um inteiro de 5 dígitos em seus dígitos individuais e mostrá-los. Reimplemente seu script utilizando um laço que, em cada iteração,'pegue' um dígito (da esquerda para a direita) utilizando os operadores // e % para, então, mostrar esse dígito."""

numero = int(input('Informe um número entre 10000 e 99999: '))
divisor = 0

if (10000 <= numero <= 99999):
    for i in range(5):
        divisor = int(10000 / 10 ** i)
        print(numero // divisor, end='   ')
        numero %= divisor
else:
    print('O número informado é inválido.')
