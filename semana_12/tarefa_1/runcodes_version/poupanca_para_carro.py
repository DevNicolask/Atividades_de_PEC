"""
Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.
"""

def calcular_meses(preco_carro):
    poupanca = 10000
    rendimento = 1.007
    aumento_carro = 1.004
    meses = 0

    while poupanca < preco_carro:
        poupanca *= rendimento
        preco_carro *= aumento_carro
        meses += 1

    return meses


def main():
    preco_carro = float(input())

    meses = calcular_meses(preco_carro)

    print(meses)


if __name__ == '__main__':
    main()