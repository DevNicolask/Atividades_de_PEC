"""
Escreva um programa que leia três números por parâmetro e mostre na tela em ordem crescente.
"""

def ordem_crescente(numero1, numero2, numero3):

    numeros = [numero1, numero2, numero3]
    numeros.sort()

    return numeros

def main():

    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
    numero3 = int(input("Digite o terceiro número inteiro: "))

    numeros_ordenados = ordem_crescente(numero1, numero2, numero3)

    print(f"Os números em ordem crescente são:")
    print(numeros_ordenados[0])
    print(numeros_ordenados[1])
    print(numeros_ordenados[2])

if __name__ == '__main__':
    main()