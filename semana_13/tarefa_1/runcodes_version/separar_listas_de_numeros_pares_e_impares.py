"""
Leia 20 números inteiros e armazene-os numa lista. Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas
"""


def main():
    numeros = [int(input()) for _ in range(20)]

    PAR = [numero for numero in numeros if numero % 2 == 0]
    IMPAR = [numero for numero in numeros if numero % 2 != 0]

    print(numeros)
    print(PAR)
    print(IMPAR)


if __name__ == "__main__":
    main()