"""
Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos (excluindo o zero).
"""

def main():
    soma = 0
    quantidade = 0

    numero = int(input())

    while numero != 0:
        soma += numero
        quantidade += 1

        numero = int(input())

    if quantidade > 0:
        media = soma / quantidade
        print(f"{media:.2f}")


if __name__ == '__main__':
    main()
