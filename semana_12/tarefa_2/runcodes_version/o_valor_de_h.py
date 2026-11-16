"""
Calcular H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n.

Escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido.
"""

def calcular_harmonica(n):
    h = 0

    for i in range(1, n + 1):
        h += 1 / i

    return h


def main():
    n = int(input())

    resultado = calcular_harmonica(n)

    print(f'{resultado:.4f}')


if __name__ == '__main__':
    main()