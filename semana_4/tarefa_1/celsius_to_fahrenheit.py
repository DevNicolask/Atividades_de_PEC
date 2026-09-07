"""Escreva um programa que leia uma temperatura em graus Celsius e mostra na tela o valor correspondente em graus Fahrenheit:
Fahrenheit = (Celsius x (9 / 5)) + 32"""

temperatura_c = float(input("Diga uma temperatura em graus Celcius: "))
temperatura_f = (temperatura_c * (9 / 5)) + 32

print(f'{temperatura_c}°C é o mesmo que {temperatura_f}° Fahrenheit')
