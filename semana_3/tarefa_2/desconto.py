"""Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado para duas casas decimais."""

preco = float(input("Digite o preço do produto: "))

preco_com_desconto = preco * 0.90

print(f"O valor com 10% de desconto é: {preco_com_desconto:.2f}")
