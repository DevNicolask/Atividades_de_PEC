"""
Escreva um programa que leia um caractere e mostre o valor booleano True (verdadeiro) se for uma letra (vogal ou consoante) ou um dígito (entre '0' e '9'), ou o valor booleano False (falso) caso contrário.
"""

def main():
    caractere = input("Digite um caractere: ").lower()
    print(f"O resultado é: {caractere in 'abcdefghijklmnopqrstuvwxyz0123456789'}")

if __name__ == '__main__':
    main()