"""
Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.
"""

def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True


def encontrar_primos(x, y):
    primos = []

    for numero in range(x, y + 1):
        if verificar_primo(numero):
            primos.append(numero)

    return primos


def main():
    x = int(input())
    y = int(input())

    resultado = encontrar_primos(x, y)

    for primo in resultado:
        print(primo)


if __name__ == '__main__':
    main()
