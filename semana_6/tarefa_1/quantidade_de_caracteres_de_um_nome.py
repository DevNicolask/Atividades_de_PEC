"""
Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.
"""

def tamanho(string):
    tamanho_string = len(string)
    return tamanho_string

def main():
    nome = input("Digite seu nome: ").strip()

    print(f"O nome possui {tamanho(nome)} caracteres.")

if __name__ == '__main__':
    main()