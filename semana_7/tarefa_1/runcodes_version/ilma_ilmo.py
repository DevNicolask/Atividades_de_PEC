"""
Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro 1 para identificar masculino e 2 para identificar feminino.
"""
def nome_concatenado(sex):
    if sex == 1:
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'

def main():
    nome = input()
    sexo = int(input())

    print(f'{nome_concatenado(sexo)} {nome}')

if __name__ == '__main__':
    main()