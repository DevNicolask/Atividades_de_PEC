"""
Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso! Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro mais próximo e imprima o resultado.
"""

def transacoes(dinheiro):
    dinheiro = round(dinheiro)
    return dinheiro

def main():
    quantidade_de_dinheiro = float(input())

    print(transacoes(quantidade_de_dinheiro))

if __name__ == '__main__':
    main()