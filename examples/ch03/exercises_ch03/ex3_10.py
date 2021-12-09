"""(Retorno de Investimento a 7%) Reimplemente o Exercício 2.12 para utilizar um laço que calcule e mostre a quantia de dinheiro que você terá ao fim dos anos 1 a 30."""

p = 1000    # montante inicial
r = 7 / 100 # taxa anual de juros

for n in range(1, 31):
    a = p * (1 + r) ** n
    print(f'Ao fim do {n}º ano, você terá ${a:.2f}')
