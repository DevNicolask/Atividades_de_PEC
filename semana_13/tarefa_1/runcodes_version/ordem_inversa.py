"""
Leia um número n e considere uma lista com n posições.

a) Preencha a lista com zeros e imprima.
b) Preencha a lista com números de 1 a n e imprima.
c) Preencha a lista com valores lidos pelo teclado e imprima.
d) Preencha a lista na ordem inversa com valores lidos pelo teclado e imprima.
"""

def main():
    n = int(input())

    lista = [0] * n
    print(lista)

    lista = [numero for numero in range(1, n + 1)]
    print(lista)

    lista = [int(input()) for _ in range(n)]
    print(lista)

    lista = []
    for _ in range(n):
        numero = int(input())
        lista.insert(0, numero)

    print(lista)


if __name__ == "__main__":
    main()