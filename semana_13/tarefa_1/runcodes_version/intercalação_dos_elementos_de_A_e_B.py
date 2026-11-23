"""
Leia duas listas A e B contendo 25 elementos inteiros cada.
Gere e imprima uma lista C de 50 elementos, intercalando
os elementos das listas A e B.
"""


def junta_listas(LISTA1, LISTA2):
    LISTA3 = []

    for i in range(25):
        LISTA3.append(LISTA1[i])
        LISTA3.append(LISTA2[i])

    return LISTA3


def main():
    A = [int(input()) for _ in range(25)]
    B = [int(input()) for _ in range(25)]

    C = junta_listas(A, B)

    print(f"{A}\n{B}\n{C}")


if __name__ == "__main__":
    main()