"""
Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos com até duas casas decimais:

Valor para pagamento à vista, com desconto de 9%.
Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
Valor da prestação para pagamento em 10 vezes, com 17% de juros.
"""

def preco_a_vista(preco):
    preco = preco - (preco * 0.09)
    return preco

def pagamento_em_cinco_vezes(preco):
    return preco / 5

def pagamento_em_dez_vezes(preco):
    preco = preco + (preco * 0.17)
    return preco / 10

def main():
    valor_comprado = float(input())

    print(f'{preco_a_vista(valor_comprado):.2f}')
    print(f'{pagamento_em_cinco_vezes(valor_comprado):.2f}')
    print(f'{pagamento_em_dez_vezes(valor_comprado):.2f}')

if __name__ == "__main__":
    main()