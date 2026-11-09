"""
Escreva um programa que leia um número inteiro e calcule o resto da divisão inteira do número lido por 5 (cinco). A seguir, de acordo com o resultado da divisão, faça o que é solicitado abaixo:

Se 0 (zero), escreva a o resultado da equação 9n + 7, onde n é o valor lido;
Se 1 (um), escreva se o valor lido é par ou ímpar;
Se 2 (dois), escreva a o resultado da equação 5n2 – 3n + 42, onde n é o valor lido;
Se 3 (três), escreva a divisão inteira do valor lido por 10;
Se 4 (quatro), escreva o quadrado do valor lido;
"""

def calculo(parametro, num):
    if parametro == 0:
        resposta = ((9 * num) + 7)
        return resposta
    
    if parametro == 1:
        if num % 2 == 0:
            return "par"
        else:
            return "ímpar"
        
    if parametro == 2:
        resposta = ((5 * num**2) - (3 * num) + 42)
        return resposta
    
    if parametro == 3:
        return num // 10
    
    if parametro == 4:
        return num**2


def main():
    numero = int(input())

    resto = numero % 5

    print(calculo(resto, numero))

if __name__ == '__main__':
    main()