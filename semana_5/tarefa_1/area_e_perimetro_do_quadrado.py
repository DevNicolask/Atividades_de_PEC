"""
Escreva um programa que ler o valor do lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.
OBS: Mostre o resultado com 4 casas decimais, alinhado à direta com 10 espaços na tela.
"""

def area(lado):
    return lado ** 2

def perimetro(lado):
    return lado * 4

def main():
    lado_do_quadrado = float(input("Digite o valor do lado do quadrado: "))

    area_do_quadrado = area(lado_do_quadrado)
    perimetro_do_quadrado = perimetro(lado_do_quadrado)

    # Exibe os resultados com 4 casas decimais,
    # alinhados à direita em 10 espaços
    print(f"A área do quadrado é: {area_do_quadrado:10.4f}")
    print(f"O perímetro do quadrado é: {perimetro_do_quadrado:10.4f}")

if __name__ == '__main__':
    main()