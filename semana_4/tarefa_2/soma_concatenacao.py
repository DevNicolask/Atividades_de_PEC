"""Escreva um programa que leia dois valores e mostre na tela, nessa ordem:

a. A soma dos números;

b. A concatenação das strings;

c. A multiplicação dos números;

d. A multiplicação como strings;

e. A divisão dos números;

f. A divisão inteira dos números;

g. A exponenciação;

h. O módulo (resto).
"""
numero_1 = float(input("Insira o primeiro número: "))
numero_2 = float(input("Insira o segundo número: "))

print(f"A soma dos números: {numero_1 + numero_2}")
print(f"A concatenação das strings: {str(numero_1)+str(int(numero_2))}")
print(f"A multiplicação dos números: {numero_1 * numero_2}")
print(f"A multiplicação como strings: {str(numero_1) * int(numero_2)}")
print(f"A divisão dos números: {numero_1 / numero_2}")
print(f"A divisão inteira dos números: {numero_1 // numero_2}")
print(f"A exponenciação: {numero_1**numero_2}")
print(f"O módulo (resto): {numero_1 % numero_2}")