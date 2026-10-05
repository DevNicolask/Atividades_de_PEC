"""
Escreva um programa que leia um número inteiro e some 5 caso o valor lido
seja par ou some 8 caso o valor lido seja ímpar. Mostre na tela o resultado
da operação.
"""

def calcular_resultado(numero):
    if numero % 2 == 0:
        return numero + 5
    else:
        return numero + 8


def main():
    numero = int(input())

    resultado = calcular_resultado(numero)

    print(f'{resultado}')


if __name__ == '__main__':
    main()