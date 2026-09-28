"""
Escreva um programa que leia o nome e o estado civil de uma pessoa, considere apenas “1” para casado e “2” para solteiro. Se a pessoa for casada, leia, também, o nome do cônjuge. Mostre quantos caracteres no total existem no(s) nome(s) lido(s).
"""

def quantidade_caracteres(nome):
    return len(nome)

def quantidade_caracteres_casado(nome, conjuge):
    return len(nome) + len(conjuge)

def main():

    nome = input().strip()
    estado_civil = int(input())

    if estado_civil == 1:
        conjuge = input().strip()
        print(f'{quantidade_caracteres_casado(nome, conjuge)}')
    else:
        print(f'{quantidade_caracteres(nome)}')
        
    

if __name__ == '__main__':
    main()