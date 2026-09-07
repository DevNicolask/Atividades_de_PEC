"""Escreva um programa que leia a idade de uma pessoa expressa em anos, meses e dias e mostra na tela a idade dessa pessoa
expressa apenas em dias. Considerar sempre os anos com 365 dias e os messes com 30 dias.
"""
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite o saldo de meses: "))
dias = int(input("Digite o saldo de dias: "))
anos *= 365
meses *= 30

print(f"Você já tem {anos + meses + dias} dias")