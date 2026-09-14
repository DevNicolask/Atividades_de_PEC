"""
Leia um número inteiro entre 1000 e 9999 e mostre o número na ordem inversa. Por exemplo, se o número lido for 5678 deverá ser mostrado 8765.
"""
def invert(numero):
    return numero[::-1]


def main():
    numero = input()
    print(f'{invert(numero)}')


if __name__ == '__main__':
    main()