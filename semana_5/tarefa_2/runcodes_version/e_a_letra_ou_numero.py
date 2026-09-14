"""
Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma letra (vogal ou consoante) ou um dígito (entre ‘0’ e ‘9’) ou valor booleano False (falso) caso contrário.
"""

def main():
    caractere = input().lower()
    print(caractere in 'abcdefghijklmnopqrstuvwxyz0123456789')


if __name__ == '__main__':
    main()