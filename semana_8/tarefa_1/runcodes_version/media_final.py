"""
Escreva um programa que leia o número de matrícula de um aluno, suas notas
em 3 provas e a média das notas obtidas nos exercícios que fazem parte da
sua avaliação. Calcule a média final usando a fórmula:

Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7

O programa deve escrever a matrícula do aluno, a média final, o conceito
correspondente e a mensagem "Aprovado" se o conceito for A, B ou C ou
"Reprovado" se o conceito for D ou E.
"""

def calcular_conceito(media):
    if media >= 9.0:
        return 'A'
    elif media >= 7.5:
        return 'B'
    elif media >= 6.0:
        return 'C'
    elif media >= 4.0:
        return 'D'
    else:
        return 'E'

def situation(cnc):
    if  cnc in 'ABC':
        return 'Aprovado'
    else:
        return 'Reprovado'

def main():
    matricula = input()
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    media_exercicios = float(input())

    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

    conceito = calcular_conceito(media_final)
    situacao = situation(conceito)

    print(f'{matricula}')
    print(f'{media_final:.2f}')
    print(f'{conceito}')
    print(f'{situacao}')


if __name__ == '__main__':
    main()



"""
2028211MTDS9876
5.90
9.85
6.50
8.00
"""