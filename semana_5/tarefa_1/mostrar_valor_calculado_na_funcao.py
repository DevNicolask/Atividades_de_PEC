"""
Escreva um programa que leia três valores inteiros (a, b e c). Calcule e mostre o resultado da função:

def calcular(a, b, c):
    return 2 * a + 5 * b - c
"""

def calcular(a, b, c):
    d = 2 * a + 5 * b - c
    return d

def main():
    n1 = int(input("Digite o primeiro valor inteiro (a): "))
    n2 = int(input("Digite o segundo valor inteiro (b): "))
    n3 = int(input("Digite o terceiro valor inteiro (c): "))

    print(f"O resultado do cálculo é: {calcular(n1, n2, n3)}")

if __name__ == '__main__':
    main()