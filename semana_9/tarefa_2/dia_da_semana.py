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
    elif num == 7:
        return "sábado"


def main():
    print("--- Dia da Semana ---")
    numero = int(input("Digite um número de 1 a 7 (1 - Domingo a 7 - Sábado): "))

    if 1 <= numero <= 7:
        dia = dia_da_semana(numero)
        print(f"\nO dia correspondente é: {dia}")
    else:
        print("\nvalor inválido")


if __name__ == '__main__':
    main()