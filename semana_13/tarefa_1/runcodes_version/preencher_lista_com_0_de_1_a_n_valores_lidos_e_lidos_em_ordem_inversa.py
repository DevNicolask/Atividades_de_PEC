"""
Escreva um programa que leia um número n. Considere uma lista com n posições, e então: 

a) preencha com 0 (zero) e imprima a lista; 

b) preencha com os números de 1 a n e imprima a lista; 

c) preencha com valores lidos pelo teclado e imprima a lista; 

d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista; dica: use insert para sempre incluir os elementos no início da lista;
"""

def main():
    n = int(input())

    lista = [0] * n
    if n == 0: lista = []
    print(lista)

    lista = [numero for numero in range(1, n + 1)]
    print(lista)

    lista = [int(input()) for _ in range(n)]
    print("SEM NOTAS" if n == 0 else lista)

    lista = []
    for _ in range(n):
        numero = int(input())
        lista.insert(0, numero)

    print(lista)


if __name__ == "__main__":
    main()