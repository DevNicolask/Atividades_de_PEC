"""Escreva um programa que leia um valor inteiro e mostra na tela no valor booleano True caso o número lido seja maior que 100 ou False caso contrário.
"""
numero = int(input("Digite um número: "))
print(f'O número é maior que 100? Resposta: {True if (numero>100) else False}')