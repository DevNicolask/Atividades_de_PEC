"""Você está fazendo uma reforma em casa e precisa calcular a quantidade de piso para sua sala e a quantidade de tinta a ser usada nas paredes. Precisa também saber qual o volume da sala em metros cúbicos para estimar a potência necessária para o ar condicionado. Para tanto, escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros e em seguida imprima:

Área do piso da sala: largura * comprimento

Volume da sala: largura * comprimento * altura

Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento
"""
altura = float(input())
comprimento = float(input())
largura = float(input())
area_do_piso = largura * comprimento
volume_da_sala = largura * comprimento * altura
area_das_paredes = 2 * altura * largura + 2 * altura * comprimento
print(area_do_piso)
print(volume_da_sala)
print(area_das_paredes)