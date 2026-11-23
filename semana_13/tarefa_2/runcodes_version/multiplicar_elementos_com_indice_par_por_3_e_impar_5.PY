"""
Leia uma lista com 100 números e ordene seus elementos.
Crie uma nova lista multiplicando os elementos de índice par por 3
e os elementos de índice ímpar por 5.
"""

def multiplica_elementos(LISTA):
    NOVA_LISTA = []

    for i in range(len(LISTA)):
        if i % 2 == 0:
            NOVA_LISTA.append(LISTA[i] * 3)
        else:
            NOVA_LISTA.append(LISTA[i] * 5)

    return NOVA_LISTA


def main():
    A = [int(input()) for _ in range(100)]

    A.sort()

    print(multiplica_elementos(A))


if __name__ == "__main__":
    main()