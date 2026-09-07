"""Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da divisão inteira dos valores."""

dividendo = float(input())
divisor = float(input())

divisao = dividendo//divisor
resto = dividendo%divisor

print(f'{divisao:.4f}')
print(f'{resto:.4f}')
