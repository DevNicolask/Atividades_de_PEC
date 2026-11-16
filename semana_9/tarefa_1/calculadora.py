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
    print("--- Calculadora Simples ---")
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    print("\nEscolha a operação desejada:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    calculo = int(input("Digite o número da operação (1 a 4): "))

    resultado = calculadora(numero1, numero2, calculo)
    print(f"\nO resultado da operação é: {resultado}")

if __name__ == '__main__':
    main()