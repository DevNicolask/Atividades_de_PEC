"""
Escreva um programa que ler o valor do lado de um quadrado. Calcule o mostre a área e o perímetro desse quadrado.
OBS: Mostre o resultado com 4 casas decimais, alinhado à direta com 10 espaços na tela.
"""
def area(lado):
    return lado**2

def perimetro(lado):
    return lado * 4

def main():
    lado_do_quadrado = float(input())
    area_do_quadrado = area(lado_do_quadrado)
    perimetro_do_quadrado = perimetro(lado_do_quadrado)

    print(f'{area_do_quadrado:10.4f}\n{perimetro_do_quadrado:10.4f}')

if __name__ == '__main__':
    main()