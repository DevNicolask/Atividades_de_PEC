"""
Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.
"""

def ordem_crescente(numero1, numero2, numero3):

    numeros = [numero1, numero2, numero3]
    numeros.sort()

    return numeros

def main():

    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())

    print(f'{ordem_crescente(numero1, numero2, numero3)}')

if __name__ == '__main__':
    main()