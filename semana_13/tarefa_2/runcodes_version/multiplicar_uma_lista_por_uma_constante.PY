"""
Leia uma quantidade indeterminada de números inteiros, terminada por 0.
Leia um valor inteiro constante e gere uma nova lista com os elementos
da lista original multiplicados pela constante.
"""

def multiplica_constante(LISTA, CONSTANTE):
    NOVA_LISTA = []

    for i in range(len(LISTA)):
        NOVA_LISTA.append(LISTA[i] * CONSTANTE)

    return NOVA_LISTA


def main():
    A = []

    while True:
        NUMERO = int(input())

        if NUMERO == 0:
            break

        A.append(NUMERO)

    CONSTANTE = int(input())

    B = multiplica_constante(A, CONSTANTE)

    print(B)


if __name__ == "__main__":
    main()