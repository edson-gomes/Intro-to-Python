"""(Aritmética, menor e maior) No exercício 2.10, você escreveu um script onde eram informados três inteiros e, então, eram mostrados a soma, a média, o produto, o menor e o maior desses valores. Reimplemente o script com um laço que pede quatro inteiros."""

import statistics

lista_inteiros = []
sentinela = 0

while sentinela < 4:
    valor = int(input(f'Informe o {sentinela + 1}º inteiro: '))
    lista_inteiros.append(valor)
    sentinela += 1

print(f'A soma dos valores informados é: {sum(lista_inteiros)}')
print(f'A média dos valores informados é: {statistics.mean(lista_inteiros)}')
print(
    f'O produto dos valores informados é: {lista_inteiros[0] * lista_inteiros[1] * lista_inteiros[2] * lista_inteiros[3]}')
print(f'O menor dos valores informados é: {min(lista_inteiros)}')
print(f'O maior dos valores informados é: {max(lista_inteiros)}')
