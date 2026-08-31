"""Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente."""
minutos_totais = int(input())

horas = minutos_totais // 60
minutos = minutos_totais % 60

print(f'{horas}h{minutos}min')