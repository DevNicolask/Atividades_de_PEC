"""
Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares; 135 tem 0 dígitos pares; 134 tem 1 dígito par.
"""

def quantidade_pares(numero):

    quantidade = 0

    if numero > 100 and numero // 100 % 2 == 0:
        quantidade = quantidade + 1

    if numero // 10 % 10 % 2 == 0:
        quantidade = quantidade + 1

    if numero % 10 % 2 == 0:
        quantidade = quantidade + 1

    return quantidade

def main():

    numero = int(input())

    print(f'{quantidade_pares(numero)}')

if __name__ == '__main__':
    main()