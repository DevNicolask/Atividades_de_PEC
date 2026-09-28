"""
Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.
"""

def mensagem_sinal(cor):

    if cor == 'V':
        return 'Siga'
    elif cor == 'A':
        return 'Atenção'
    else:
        return 'Pare'

def main():

    cor = input().upper()

    print(f'{mensagem_sinal(cor)}')

if __name__ == '__main__':
    main()