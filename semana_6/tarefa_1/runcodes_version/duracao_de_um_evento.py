"""
Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).
"""
def horas(seg):
    hr = seg // 3600
    if hr < 10:
        hr = '0'+ str(hr)
    return hr

def minutos(seg):
    seg %= 3600
    min = seg // 60
    if min < 10:
        min = '0'+ str(min)
    return min

def segundos(seg):
    seg %= 60
    if seg < 10:
        seg = '0'+ str(seg)
    return seg

def main():
    tempo = int(input())

    print(f'{horas(tempo):2}:{minutos(tempo):2}:{segundos(tempo):2}')

if __name__ == '__main__':
    main()
