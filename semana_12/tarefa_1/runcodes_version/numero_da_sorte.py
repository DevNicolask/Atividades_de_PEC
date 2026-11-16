"""
O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um programa que leia a data de nascimento, digitada no formato ddmmaaaa (um número inteiro com 8 dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989 e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).
"""

def calcular_numero_da_sorte(data):
    soma = 0

    while data > 0:
        digito = data % 10
        soma += digito
        data //= 10

    return soma


def main():
    data = int(input())

    numero_sorte = calcular_numero_da_sorte(data)

    print(numero_sorte)


if __name__ == '__main__':
    main()