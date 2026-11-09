"""
Escreva um programa que leia dois valores e uma das seguintes operações, codificadas dessa forma, será executada:

1 – Adição

2 – Subtração

3 – Multiplicação

4 – Divisão

Calcule e escreva o resultado dessa operação sobre os dois valores lidos.
"""

def calculadora(num1, num2, parametro):
    if parametro == 1:
        return num1 + num2
    elif parametro == 2:
        return num1 - num2
    elif parametro == 3:
        return num1 * num2
    elif parametro == 4:
        return num1 / num2
    
def main():
    numero1 = float(input())
    numero2 = float(input())
    calculo = int(input())

    print(calculadora(numero1, numero2, calculo))

if __name__ == '__main__':
    main()