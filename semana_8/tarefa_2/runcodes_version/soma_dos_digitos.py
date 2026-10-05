"""
Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos
para os números entre 0 (zero) e 100 mil ou -1 para outros valores.

Exemplo:
Em 16759 a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31.
Em 136759 o valor é maior que 100 mil e deve retornar -1.
Em -100 o valor é negativo e deve retornar -1.
"""

def somar_digitos(numero):
    if numero <= 0 or numero >= 100000:
        return -1

    soma = 0

    while numero > 0:
        soma += numero % 10
        numero //= 10

    return soma


def main():
    numero = int(input())

    resultado = somar_digitos(numero)

    print(f'{resultado}')


if __name__ == '__main__':
    main()