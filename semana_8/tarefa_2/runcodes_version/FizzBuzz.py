"""
Escreva um programa que leia um número inteiro positivo e escreva na tela:

FIZZ se o número é divisível por três;

BUZZ se o número é divisível por cinco;

FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo;

O próprio número caso não seja divisível por três ou por cinco.

Para cada número lido apenas uma resposta deve ser impressa.
"""

def verificar_numero(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FIZZBUZZ'
    elif numero % 3 == 0:
        return 'FIZZ'
    elif numero % 5 == 0:
        return 'BUZZ'
    else:
        return numero


def main():
    numero = int(input())

    resultado = verificar_numero(numero)

    print(f'{resultado}')


if __name__ == '__main__':
    main()