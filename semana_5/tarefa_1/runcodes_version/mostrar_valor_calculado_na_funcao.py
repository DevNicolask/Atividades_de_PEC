"""Escreva um programa que ler três valores inteiros (a, b, e c). Calcule o mostre o resultado da função:

def calcular(a, b, c):
    return 2 * a + 5 * b - c
"""
def calcular(a, b, c):
    d = 2 * a + 5 * b - c
    return d

def main():
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    print(calcular(n1,n2,n3))

if __name__ == '__main__':
    main()