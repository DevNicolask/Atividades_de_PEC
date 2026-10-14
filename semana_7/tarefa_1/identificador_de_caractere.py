"""
Escreva um programa que leia um caractere e mostre uma das mensagens: “vogal”, “consoante”, “número” ou “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros são considerados “símbolo”.
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

    caractere = input("Digite um caractere: ")

    print(f"O caractere digitado é: {identificar_caractere(caractere)}")

if __name__ == '__main__':
    main()