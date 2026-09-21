"""
Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total! Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.
"""

def total_da_compra(banana, maca):
    preco = banana * 2 + maca * 3
    return preco

def main():
    preco_de_uma_maca = float(input())
    preco_de_uma_banana = float(input())

    print(f'{total_da_compra(preco_de_uma_banana, preco_de_uma_maca):.2f}')

if __name__ == '__main__':
    main()