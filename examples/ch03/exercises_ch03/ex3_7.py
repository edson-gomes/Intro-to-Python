"""(Tabela de quadrados e cubos) No exercício 2.8, você escreveu um script para calcular os quadrados e cubos dos números de 0 a 5 e, então, imprimiu os valores resultantes em formato tabular. Reimplemente o script utilizando um laço for e as opções de f-string aprendidos nesse capítulo para criar a tabela a seguir, com os números aninhados à direta em cada coluna."""

# número    quadrado    cubo
#      0           0       0
#      1           1       1
#      2           4       8
#      3           9      27
#      4          16      64
#      5          25     125

print('número', '\tquadrado', '\tcubo')

for numero in range(6):
    # utilizada uma sequência de escape \t para separar as colunas
    print(f'{numero:>6}\t{(numero ** 2):>8}\t{(numero ** 3):>4}')
