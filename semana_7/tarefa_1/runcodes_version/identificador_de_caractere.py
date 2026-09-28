"""
Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.
"""

def identificar_caractere(caractere):

    if caractere in 'aeiouAEIOU':
        return 'vogal'
    elif caractere.isalpha():
        return 'consoante'
    elif caractere.isdigit():
        return 'número'
    else:
        return 'símbolo'

def main():

    caractere = input()

    print(f'{identificar_caractere(caractere)}')

if __name__ == '__main__':
    main()