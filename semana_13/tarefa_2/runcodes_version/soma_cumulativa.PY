"""
Leia uma quantidade indeterminada de números reais, terminada por 0.
Gere uma nova lista com a soma cumulativa dos elementos da lista original.
"""

def soma_cumulativa(LISTA):
    NOVA_LISTA = []
    soma = 0

    for i in range(len(LISTA)):
        soma += LISTA[i]
        NOVA_LISTA.append(int(soma))

    return NOVA_LISTA


def main():
    A = []

    while True:
        numero = float(input())

        if numero == 0:
            break

        A.append(numero)

    print(soma_cumulativa(A))



if __name__ == "__main__":
    main()