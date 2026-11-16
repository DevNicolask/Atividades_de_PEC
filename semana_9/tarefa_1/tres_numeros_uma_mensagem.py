"""
Escreva um programa que leia 3 (três) números inteiros e escreva uma das mensagens abaixo, de acordo com os valores lidos:

Todos os valores são diferentes;

Existem dois valores iguais e um diferente;

Todos os valores são iguais.
"""

def comparar_numeros(num1, num2, num3):
    if num1 == num2 == num3:
        return "iguais"
    elif num1 == num2 or num1 == num3 or num2 == num3:
        return "dois_iguais"
    else:
        return 0

def main():
    numero1 = int(input())
    numero2 = int(input())
    numero3 = int(input())

    valores = comparar_numeros(numero1, numero2, numero3)

    if valores == "iguais":
        print("Todos os valores são iguais")
    elif valores == "dois_iguais":
        print("Existem dois valores iguais e um diferente")
    else:
        print("Todos os valores são diferentes")

if __name__ == '__main__':
    main()