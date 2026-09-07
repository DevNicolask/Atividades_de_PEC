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
numero_1 = float(input())
numero_2 = float(input())

print(numero_1 + numero_2)
print(str(numero_1)+str(int(numero_2))) 
print(numero_1 * numero_2)
print(str(numero_1) * int(numero_2))
print(numero_1 / numero_2)
print(numero_1 // numero_2)
print(numero_1**numero_2)
print(numero_1 % numero_2)