"""Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores."""

dividendo = float(input("Digite o dividendo (número que será dividido): "))
divisor = float(input("Digite o divisor (número que vai dividir): "))

divisao = dividendo // divisor
resto = dividendo % divisor

print(f"O resultado da divisão inteira é: {divisao:.4f}")
print(f"O resto da divisão é: {resto:.4f}")
