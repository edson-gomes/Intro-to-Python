"""(O teste de Turing) O grande matemático britânico Alan Turing propôs um teste simples para determinar se máquinas poderiam exibir comportamento inteligente. Um usuário senta-se em frente a um computador e participa da mesma conversa em texto com um humano operando outro computador e um computador operando de forma independente. Se o usuário não puder distinguir quais respostas vêm do humano e quais repostas vêm do computador, então é plausível dizer que o computador está exibindo comportamento inteligente.
Crie um script que executa o papel de computador independente, dando ao usuário um diagnóstico médico simples. O script deve perguntar ao usuário 'Qual é o seu problema?'. Quando o usuário responder e pressionar Enter, o script deve simplesmente ignorar a resposta e, então, perguntar ao usuário 'Você já teve esse problema antes? (sim ou não)'. Se o usuário inserir 'sim', imprima 'Bem, você está com esse problema novamente.'. Se o usuário responder 'não', imprima 'Bem, agora você tem.'
Essa conversa convenceria o usuário que a entidade com quem estava interagindo se comportava de maneira inteligente? Por quê?"""

input('Qual é o seu problema? ')
resposta = input('Você já teve esse problema antes? (sim ou não): ' )

if resposta == 'sim':
    print('Bem, você está com esse problema novamente.')
elif resposta == 'não':
    print('Bem, agora você tem.')

""" A conversa provavelmente não conveceria o usuário, porque, além de não oferecer um diagnóstico muito inteligente, não são levadas em consideração respostas diferentes de sim ou não, ou mesmo respostas em branco."""