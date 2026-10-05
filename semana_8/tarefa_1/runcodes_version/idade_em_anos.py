"""
Escreva um programa que leia, separadamente, dia, mês e ano da data atual.
Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva
a idade exata em anos.
"""

def calcular_idade(dia_atual, mes_atual, ano_atual, dia_nasc, mes_nasc, ano_nasc):
    idade = ano_atual - ano_nasc

    if (mes_atual, dia_atual) < (mes_nasc, dia_nasc):
        idade -= 1

    return idade


def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())

    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())

    idade = calcular_idade(
        dia_atual, mes_atual, ano_atual,
        dia_nasc, mes_nasc, ano_nasc
    )

    print(f'{idade}')


if __name__ == '__main__':
    main()