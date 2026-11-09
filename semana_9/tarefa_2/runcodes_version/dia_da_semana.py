"""
Escreva um programa que leia um número e exiba o dia correspondente da semana. (1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve aparecer “valor inválido”.
"""

def dia_da_semana(num):
    if num == 1:
        return "domingo"
    elif num == 2:
        return "segunda-feira"
    elif num == 3:
        return "terça-feira"
    elif num == 4:
        return "quarta-feira"
    elif num == 5:
        return "quinta-feira"
    elif num == 6:
        return "sexta-feira"
    else:
        return "sábado"

def main():
    numero = int(input())

    if 1 <= numero <= 7:
        print(dia_da_semana(numero))
    else:
        print("valor inválido")

if __name__ == '__main__':
    main()