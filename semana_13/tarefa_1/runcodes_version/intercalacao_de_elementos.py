"""
Leia duas listas A e B contendo 25 elementos inteiros cada.
Gere e imprima uma lista C de 50 elementos, intercalando
os elementos das listas A e B.
"""

def main():
    A = [int(input()) for _ in range(25)]
    B = [int(input()) for _ in range(25)]

    C = []

    for i in range(25):
        C.append(A[i])
        C.append(B[i])

    print(C)


if __name__ == "__main__":
    main()