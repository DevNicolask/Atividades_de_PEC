"""
Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:

o maior número lido;
o menor número lido;
a média aritmética dos números lidos.
"""

def maior_numero(num_1, num_2, num_3, num_4, num_5):
    return max(num_1, num_2, num_3, num_4, num_5)

def menor_numero(num_1, num_2, num_3, num_4, num_5):
    return min(num_1, num_2, num_3, num_4, num_5)

def media(num_1, num_2, num_3, num_4, num_5):
    media = (num_1 + num_2 + num_3 + num_4 + num_5) / 5
    return media

def main():
    numero_1 = int(input("Digite o primeiro número inteiro: "))
    numero_2 = int(input("Digite o segundo número inteiro: "))
    numero_3 = int(input("Digite o terceiro número inteiro: "))
    numero_4 = int(input("Digite o quarto número inteiro: "))
    numero_5 = int(input("Digite o quinto número inteiro: "))

    print(f"O maior número lido é: {maior_numero(numero_1, numero_2, numero_3, numero_4, numero_5)}")
    print(f"O menor número lido é: {menor_numero(numero_1, numero_2, numero_3, numero_4, numero_5)}")
    print(f"A média aritmética dos números é: {media(numero_1, numero_2, numero_3, numero_4, numero_5)}")

if __name__ == "__main__":
    main()