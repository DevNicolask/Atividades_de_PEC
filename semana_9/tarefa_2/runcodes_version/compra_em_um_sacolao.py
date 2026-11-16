"""
Um sacolão está vendendo frutas com a seguinte tabela de preços:

Item       Até 5Kg    Acima de 5Kg
Morango    R$ 2,50    R$ 2,20
Maçã       R$ 1,80    R$ 1,50

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.
"""

def calcular_valor_morangos(kg):
    if kg <= 5:
        return kg * 2.50
    else:
        return kg * 2.20


def calcular_valor_macas(kg):
    if kg <= 5:
        return kg * 1.80
    else:
        return kg * 1.50


def calcular_desconto(total, quantidade):
    if quantidade > 8 or total > 25:
        total *= 0.90

    return total


def calcular_compra(morangos, macas):
    valor_morangos = calcular_valor_morangos(morangos)
    valor_macas = calcular_valor_macas(macas)

    total = valor_morangos + valor_macas
    quantidade = morangos + macas

    return calcular_desconto(total, quantidade)


def main():
    morangos = float(input())
    macas = float(input())

    total = calcular_compra(morangos, macas)

    print(f'R$ {total:.2f}')


if __name__ == '__main__':
    main()