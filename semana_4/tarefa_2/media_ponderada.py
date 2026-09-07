"""Escreva um programa que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas são 2, 3 e 5. Fórmula para o cálculo da média final é: média ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10"""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro e último número: "))
media_ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10

print(f'A média ponderada desses números é: {media_ponderada}')