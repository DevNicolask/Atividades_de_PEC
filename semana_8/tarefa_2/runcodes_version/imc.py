"""
O índice de massa corporal (IMC) é uma medida internacional usada para
calcular se uma pessoa está no peso ideal. O IMC é determinado pela divisão
da massa do indivíduo pelo quadrado de sua altura, em que a massa está em
quilogramas e a altura em metros. Escreva um programa que leia a massa
(o peso) e a altura de uma pessoa e calcula o IMC de uma pessoa, e depois,
mostra uma das seguintes mensagens:

IMC < 18,5: Abaixo do peso
IMC < 25: Peso normal
IMC < 30: Sobrepeso
IMC < 35: Obeso leve
IMC < 40: Obeso moderado
IMC >= 40: Obeso mórbido
"""


def calcular_imc(massa, altura):
    return massa / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 35:
        return 'Obeso leve'
    elif imc < 40:
        return 'Obeso moderado'
    else:
        return 'Obeso mórbido'


def main():
    massa = float(input())
    altura = float(input())

    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)

    print(f'{imc:.2f}')
    print(classificacao)


if __name__ == '__main__':
    main()