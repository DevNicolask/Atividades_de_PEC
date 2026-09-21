"""
Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:

o maior número lido;
o menor número lido;
a média aritmética dos números lidos
"""

def maior_numero(num_1, num_2, num_3, num_4, num_5):
    return max(num_1, num_2, num_3, num_4, num_5)

def menor_numero(num_1, num_2, num_3, num_4, num_5):
    return min(num_1, num_2, num_3, num_4, num_5)

def media(num_1, num_2, num_3, num_4, num_5):
    media = (num_1 + num_2 + num_3 + num_4 + num_5) / 5
    return media

def main():
    numero_1 = int(input())
    numero_2 = int(input())
    numero_3 = int(input())
    numero_4 = int(input())
    numero_5 = int(input())

    print(maior_numero(numero_1, numero_2, numero_3, numero_4, numero_5))
    print(menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5))
    print(media(numero_1, numero_2, numero_3, numero_4, numero_5))

if __name__ == "__main__":
    main()