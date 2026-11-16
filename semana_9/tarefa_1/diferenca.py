"""
Escreva um programa que leia 3 valores inteiros. Determine se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.
"""

def comparar_numeros(num1, num2, num3):
    diferenca1 = negativo(num1 - num2)
    diferenca2 = negativo(num1 - num3)
    if diferenca1 < diferenca2:
        return diferenca1
    else:
        return diferenca2

def negativo(numero):
    if numero < 0:
        return -numero
    else: 
        return numero

def main():
    print("--- Comparador de Diferença ---")
    numero1 = int(input("Digite o primeiro número inteiro (referência): "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))

    menor_diferenca = comparar_numeros(numero1, numero2, numero3)
    print(f"\nA menor diferença em relação ao primeiro número é: {menor_diferenca}")

if __name__ == '__main__':
    main()