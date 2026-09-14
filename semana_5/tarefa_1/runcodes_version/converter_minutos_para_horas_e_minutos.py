"""
Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertidade para horas e minutos. Por exemplo, 220 minutos é equivalente 3 horas e 40 minutos.
"""
def horas(h):
    return h // 60

def minutos(h):
    return h % 60

def main():
    tempo = int(input())

    print(f'{horas(tempo)}:{minutos(tempo)}')


if __name__ == '__main__':
    main()