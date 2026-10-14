"""
Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao caractere lido.
"""

def codigo(chr):
    return ord(chr)

def main():
    char = input("Digite um único caractere: ")

    print(f"O código numérico correspondente ao caractere é: {codigo(char)}")

if __name__ == '__main__':
    main()