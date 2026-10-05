"""
Escreva um programa que leia 5 números inteiros e escreva o maior e o menor
deles. Considere que todos os valores são diferentes. Não use as funções
min() e max().
"""

def encontrar_maior_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    return maior, menor


def main():
    numeros = []

    for i in range(5):
        numeros.append(int(input()))

    maior, menor = encontrar_maior_menor(numeros)

    print(f'{maior}')
    print(f'{menor}')


if __name__ == '__main__':
    main()