"""
Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:

N! = 1 x 2 x 3 x ... x N-1 x N
0! = 1
"""

def calcular_fatorial(numero):
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


def main():
    numero = int(input())

    resultado = calcular_fatorial(numero)

    print(resultado)


if __name__ == '__main__':
    main()