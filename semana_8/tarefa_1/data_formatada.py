"""
Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
"""

def comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    if (ano1, mes1, dia1) > (ano2, mes2, dia2):
        return 1
    else:
        return 2

def main():
    dia1 = int(input("Digite o dia da primeira data: "))
    mes1 = int(input("Digite o mês da primeira data: "))
    ano1 = int(input("Digite o ano da primeira data: "))

    dia2 = int(input("Digite o dia da segunda data: "))
    mes2 = int(input("Digite o mês da segunda data: "))
    ano2 = int(input("Digite o ano da segunda data: "))

    data_recente = comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2)

    if data_recente == 1:
        print(f"A data mais recente é: {dia1}/{mes1}/{ano1}")
    else:
        print(f"A data mais recente é: {dia2}/{mes2}/{ano2}")

if __name__ == '__main__':
    main()