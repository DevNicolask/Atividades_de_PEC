"""
Escreva um programa que leia a altura e o sexo de uma pessoa, considere
1 para 'homens' e 2 para 'mulheres'. Usando duas casas decimais, calcule
e mostre o peso ideal utilizando as seguintes fórmulas:

Para homens: (72.7 * altura) - 58

Para mulheres: (62.1 * altura) - 44.7
"""

def calcular_peso_ideal(altura, sexo):
    if sexo == 1:
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7


def main():
    altura = float(input())
    sexo = int(input())

    peso_ideal = calcular_peso_ideal(altura, sexo)

    print(f'{peso_ideal:.2f}')


if __name__ == '__main__':
    main()