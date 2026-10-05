"""
Escreva um programa que leia 5 números inteiros, calcule e mostre a média
e escreva os que são maiores que a média. Considere duas casas decimais.
"""

def calcular_media(numeros):
    return sum(numeros) / 5


def main():
    numeros = []

    for i in range(5):
        numeros.append(int(input()))

    media = calcular_media(numeros)

    print(f'{media:.1f}')

    for numero in numeros:
        if numero > media:
            print(numero)


if __name__ == '__main__':
    main()