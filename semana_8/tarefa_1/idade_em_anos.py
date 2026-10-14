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
    dia_atual = int(input("Digite o dia da data atual: "))
    mes_atual = int(input("Digite o mês da data atual: "))
    ano_atual = int(input("Digite o ano da data atual: "))

    dia_nasc = int(input("Digite o dia do seu nascimento: "))
    mes_nasc = int(input("Digite o mês do seu nascimento: "))
    ano_nasc = int(input("Digite o ano do seu nascimento: "))

    idade = calcular_idade(
        dia_atual, mes_atual, ano_atual,
        dia_nasc, mes_nasc, ano_nasc
    )

    print(f"Sua idade é: {idade} anos.")

if __name__ == '__main__':
    main()
