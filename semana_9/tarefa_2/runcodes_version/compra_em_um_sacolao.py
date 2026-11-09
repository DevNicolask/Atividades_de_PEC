"""
Um sacolão está vendendo frutas com a seguinte tabela de preços:

Item	Até 5Kg	Acima de 5Kg
Morango	R$ 2,50	R$ 2,20
Maça	R$ 1,80	R$ 1,50

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um programa que leia a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

def analise_do_valor(morangos, macas):
    if morangos <= 5:
        valor_morangos = morangos * 2.5
    else:
        valor_morangos = morangos * 2.2

    if macas <= 5:
        valor_macas = (macas * 1.8)
    else:
        valor_macas = (macas * 1.5)

    valor_total = valor_macas + valor_morangos

    return valor_total

def main():
    peso_dos_morangos = float(input())
    peso_das_macas = float(input())

    valor_das_frutas = analise_do_valor(peso_dos_morangos, peso_das_macas)

    if valor_das_frutas > 25.0 or (peso_dos_morangos + peso_das_macas) > 8.0:
        print(f"{valor_das_frutas * 0.9:.2f}")
    else:
        print(f"{valor_das_frutas:.2f}")

if __name__ == '__main__':
    main()