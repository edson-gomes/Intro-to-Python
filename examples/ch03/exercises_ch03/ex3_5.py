# (Declarações if...else) Reimplemente o script de Fig. 2.1 usando três declarações if...else ao invés de seis declarações if. [Dica: por exemplo, pense em == e != como testes "contrários".]

print('Informe dois números inteiros e vou dizer',
      'as relações que eles satisfazem.')

primeiro_numero = int(input('Informe o primeiro número inteiro: '))
segundo_numero = int(input('Informe o segundo número inteiro: '))

if primeiro_numero == segundo_numero:
    print(primeiro_numero, 'é igual a', segundo_numero)
else:
    print(primeiro_numero, 'não é igual a', segundo_numero)

if primeiro_numero < segundo_numero:
    print(primeiro_numero, 'é menor que', segundo_numero)
else:
    print(primeiro_numero, 'é maior que', segundo_numero)

if primeiro_numero <= segundo_numero:
    print(primeiro_numero, 'é menor que ou igual a', segundo_numero)
else:
    print(primeiro_numero, 'é maior que ou igual a', segundo_numero)
