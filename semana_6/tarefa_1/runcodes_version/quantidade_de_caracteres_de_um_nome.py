"""
Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.
"""
def tamanho(string):
    tamanho_string = len(string)
    return tamanho_string

def main():
    nome = input().strip()

    print(tamanho(nome))

if __name__ == '__main__':
    main()
