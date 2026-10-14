"""
Escreva um programa que leia um número e mostre o valor booleano True (verdadeiro) se o número for ímpar ou o valor booleano False (falso) caso contrário.
"""

def impar_ou_par(num):
    return num % 2 != 0

def main():
    numero = int(input("Digite um número inteiro: "))

    print(f'{impar_ou_par(numero)}')

if __name__ == '__main__':
    main()