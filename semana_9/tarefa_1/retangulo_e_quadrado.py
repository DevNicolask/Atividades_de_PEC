"""
Escreva um programa que leia dois valores que correspondem à base e a altura de um retângulo. O programa deve inicialmente verificar se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprima a palavra QUADRADO e caso seja um retângulo, mostre o perímetro (soma de todos os lados) e a área (base vezes a altura) do retângulo. Separe esses valores com um hífen.
"""

def quadrado(lado1, lado2):
    if lado1 == lado2:
        return True
    else: 
        return False

def retangulo_perimetro(lado1, lado2):
    perimetro = 2 * (lado1 + lado2)
    return perimetro

def retangulo_area(lado1, lado2):
    area = lado1 * lado2
    return area
    
def main():
    print("--- Verificador de Quadrado ou Retângulo ---")
    base = int(input("Digite o valor da base: "))
    altura = int(input("Digite o valor da altura: "))

    if quadrado(base, altura):
        print("\nResultado: QUADRADO")
    else:
        perimetro = retangulo_perimetro(base, altura)
        area = retangulo_area(base, altura)
        print(f"\nResultado (Perímetro - Área): {perimetro} - {area}")

if __name__ == '__main__':
    main()