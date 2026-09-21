"""
Um alienígena chamado Zob precisa de ajuda para converter anos terrestres em anos espaciais! Sabendo que 1 ano
terrestre equivale a meio ano espacial, calcule e imprima uma idade inserida pelo usuário em anos espaciais.
"""

def zob(ano):
    ano_espacial = ano // 2
    return ano_espacial

def main():
    idade_terrestre = int(input())

    print(zob(idade_terrestre))

if __name__ == '__main__':
    main()