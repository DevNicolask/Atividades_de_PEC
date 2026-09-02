"""Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente."""

minutos_totais = int(input("Digite a quantidade total de minutos: "))

horas = minutos_totais // 60
minutos = minutos_totais % 60

print(f"O tempo convertido é: {horas}h{minutos}min")
