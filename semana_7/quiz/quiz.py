"""
Projeto 03 - Quiz

Crie um quiz com perguntas de múltipla escolha. O jogador deve escolher
uma alternativa e receber uma mensagem informando se acertou ou errou.
"""

def test_resposta_diferente(resposta):
    while resposta not in ('a', 'b', 'c'):
        print('Você não escolheu a, ou, b ou c')
        resposta = input().lower()
    return resposta

def pergunta1():

    print('''
Q1 - No python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variável
c - uma caixa de sapatos
''')

    resposta = input().lower()
    resposta = test_resposta_diferente(resposta)

    while resposta not in ('a', 'b', 'c'):
        print('Você não escolheu a, ou, b ou c')
        resposta = input().lower()

    if resposta == 'a':
        print('Não - texto é um tipo de dado :(')
        return 0
    elif resposta == 'b':
        print('Correto :)')
        return 1
    elif resposta == 'c':
        print('Não seja bobinho! :(')
        return 0

def pergunta2():

    print('''
Q2 - Qual comando usamos para mostrar algo na tela em Python?
a - input()
b - print()
c - show()
''')

    resposta = input().lower()
    resposta = test_resposta_diferente(resposta)

    if resposta == 'a':
        print('Não - o input() recebe dados do usuário pelo teclado :(')
        return 0
    elif resposta == 'b':
        print('Correto :)')
        return 1
    elif resposta == 'c':
        print('Não - esse comando não existe em Python :(')
        return 0

def pergunta3():

    print('''
Q3 - Qual função usamos para receber uma informação do usuário?
a - print()
b - input()
c - return()
''')

    resposta = input().lower()
    resposta = test_resposta_diferente(resposta)

    if resposta == 'a':
        print('Não - o print() é usado para mostrar informações na tela :(')
        return 0
    elif resposta == 'b':
        print('Correto :)')
        return 1
    elif resposta == 'c':
        print('Não - o return é usado para retornar um valor de uma função :(')
        return 0

def pergunta4():

    print('''
Q4 - Qual símbolo usamos para verificar se duas coisas são iguais?
a - =
b - ==
c - !=
''')

    resposta = input().lower()
    resposta = test_resposta_diferente(resposta)

    if resposta == 'a':
        print('Não - o = é usado para atribuir um valor a uma variável :(')
        return 0
    elif resposta == 'b':
        print('Correto :)')
        return 1
    elif resposta == 'c':
        print('Não - o != verifica se duas coisas são diferentes :(')
        return 0

def pergunta5():

    print('''
Q5 - Qual dessas opções é uma estrutura de decisão em Python?
a - if
b - input
c - print
''')

    resposta = input().lower()
    resposta = test_resposta_diferente(resposta)

    if resposta == 'a':
        print('Correto :)')
        return 1
    elif resposta == 'b':
        print('Não - input() é usado para receber informações do usuário :(')
        return 0
    elif resposta == 'c':
        print('Não - print() é usado para mostrar informações na tela :(')
        return 0


def main():

    pontos = 0

    pontos = pontos + pergunta1()
    pontos = pontos + pergunta2()
    pontos = pontos + pergunta3()
    pontos = pontos + pergunta4()
    pontos = pontos + pergunta5()

    print(f'\nVocê fez {pontos} de 5 pontos!')

    if pontos == 5:
        print('Parabéns!!! Você acertou tudo! :)')
    elif pontos >= 3:
        print('Muito bem! Você foi bem no quiz! :)')
    else:
        print('Continue estudando e tente novamente, vai dar certo!')

if __name__ == '__main__':
    main()