"""
Escreva um programa que leia um caractere e mostre o valor booleano True (verdadeiro) se for uma consoante ou o valor booleano False (falso) caso contrário.
"""

def main():
    caractere = input("Digite um caractere: ").lower()
    print(caractere in 'bcdfghjklmnpqrstvwxyz')

if __name__ == '__main__':
    main()