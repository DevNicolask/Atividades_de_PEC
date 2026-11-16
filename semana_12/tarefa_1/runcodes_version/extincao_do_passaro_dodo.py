"""
O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% dos animais vivos no começo do ano morreram e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.

Escreva um programa que leia a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano (apenas a parte inteira dos números, separados por vírgula). O programa encerra sua execução quando a população total cai para menos de 10% da população original.
"""

from math import ceil


def calcular_nascimentos(populacao):
    return int(populacao * 0.01)


def calcular_mortes(populacao):
    return int(populacao * 0.06)


def calcular_populacao(populacao, nascimentos, mortes):
    return populacao + nascimentos - mortes


def simular_populacao(populacao):
    populacao_original = populacao
    limite = populacao_original * 0.10

    while populacao >= limite:
        nascimentos = calcular_nascimentos(populacao)
        mortes = calcular_mortes(populacao)

        populacao = calcular_populacao(populacao, nascimentos, mortes)

        print(f'{nascimentos}, {mortes}, {populacao}')


def main():
    populacao = int(input())

    simular_populacao(populacao)


if __name__ == '__main__':
    main()