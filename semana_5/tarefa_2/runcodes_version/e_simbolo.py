"""
Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o que não é letra ou número) ou o valor booleano False (falso) caso contrário.
"""

def main():
    caractere = input().lower()
    print(caractere not in 'abcdefghijklmnopqrstuvwxyz0123456789')


if __name__ == '__main__':
    main()