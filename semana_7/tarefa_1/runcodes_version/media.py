"""
Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso, se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.
"""

def calcular_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    if nota3 > 8:
        media = media + 1

    if media > 10:
        media = 10

    return media

def main():

    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    print(f'{calcular_media(nota1, nota2, nota3)}')

if __name__ == '__main__':
    main()