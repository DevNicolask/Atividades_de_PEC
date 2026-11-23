"""
Leia uma lista de 10 números inteiros. Mostre os números, sua soma e sua multiplicação.
"""

def main():
    numeros = [int(input()) for _ in range(10)]

    soma = sum(numeros)

    multiplicacao = 1
    for numero in numeros:
        multiplicacao *= numero

    print(numeros)
    print(soma)
    print(multiplicacao)


if __name__ == "__main__":
    main()