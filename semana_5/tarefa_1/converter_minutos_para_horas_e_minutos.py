"""
Escreva um programa que leia uma determinada quantidade de minutos e informe essa quantidade convertida para horas e minutos. Por exemplo, 220 minutos é equivalente a 3 horas e 40 minutos.
"""

def horas(h):
    return h // 60

def minutos(h):
    return h % 60

def main():
    tempo = int(input("Digite a quantidade de minutos: "))

    print(f"O tempo convertido é {horas(tempo)} horas e {minutos(tempo)} minutos.")

if __name__ == '__main__':
    main()