"""
A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...).

Escreva um programa que leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n sempre será maior ou igual a 2.
"""

def calcular_fibonacci(num):
    primeiro = 0
    segundo = 1

    termos = []

    for i in range(num):
        termos.append(primeiro)

        proximo = primeiro + segundo
        primeiro = segundo
        segundo = proximo

    return termos


def main():
    numero = int(input())

    resultado = calcular_fibonacci(numero)

    print(*resultado, sep=', ')


if __name__ == '__main__':
    main()