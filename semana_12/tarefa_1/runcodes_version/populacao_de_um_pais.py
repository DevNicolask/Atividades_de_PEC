"""
Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3% ao ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a população do país A.
"""

def calcular_tempo(populacao_a, populacao_b):
    taxa_a = 1.02
    taxa_b = 1.03
    anos = 0

    if populacao_b > populacao_a:
        while populacao_a <= populacao_b:
            populacao_b *= taxa_a
            populacao_a *= taxa_b
            anos += 1
    else:
        while populacao_b <= populacao_a:
            populacao_a *= taxa_a
            populacao_b *= taxa_b
            anos += 1

    return anos


def main():
    populacao_a = int(input())
    populacao_b = int(input())

    print(calcular_tempo(populacao_a, populacao_b))


if __name__ == '__main__':
    main()