"""
Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.

- Nenhum dígito é ímpar.
- Apenas um dígito é ímpar.
- Os dois dígitos são ímpares.
"""

def verificar_digitos(numero):

    quantidade = 0

    if numero // 10 % 2 != 0:
        quantidade = quantidade + 1

    if numero % 10 % 2 != 0:
        quantidade = quantidade + 1

    if quantidade == 0:
        return 'Nenhum dígito é ímpar.'
    elif quantidade == 1:
        return 'Apenas um dígito é ímpar.'
    else:
        return 'Os dois dígitos são ímpares.'

def main():

    numero = int(input())

    print(f'{verificar_digitos(numero)}')

if __name__ == '__main__':
    main()