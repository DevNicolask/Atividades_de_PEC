"""
Escreva um programa que leia um número inteiro menor que 1000 e mostre por extenso a quantidade de centenas, dezenas e unidades do número lido, observando os termos no plural, a colocação do "e" ou da vírgula entre valores e o ponto “.” no final da frase. Exemplos:

521 = cinco centenas, duas dezenas e uma unidade.
107 = uma centena e sete unidades.
80 = oito dezenas.
"""

def tamanho_do_numero(num):
    comprimento = 0

    while num > 0:
        comprimento += 1
        num //= 10
    return comprimento

def escreve_unidades(algarismo):
    if algarismo == 1:
        return 'uma unidade'
    else:
        return numero_por_extenso(algarismo) + ' unidades'

def escreve_dezenas(algarismo):
    if algarismo == 1:
        return 'uma dezena'
    else:
        return numero_por_extenso(algarismo) + ' dezenas'

def escreve_centenas(algarismo):
    if algarismo == 1:
        return 'uma centena'
    else:
        return numero_por_extenso(algarismo) + ' centenas'

def numero_por_extenso(alg):
    if alg == 1:
        return 'uma'
    elif alg == 2:
        return 'duas'
    elif alg == 3:
        return 'tres'
    elif alg == 4:
        return 'quatro'
    elif alg == 5:
        return 'cinco'
    elif alg == 6:
        return 'seis'
    elif alg == 7:
        return 'sete'
    elif alg == 8:
        return 'oito'
    elif alg == 9:
        return 'nove'

def escrever_numero_por_extenso(num, tam):
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10

    if tam == 1:
        print(f'{escreve_unidades(unidade)}.')
    elif tam == 2 and unidade == 0:
        print(f'{escreve_dezenas(dezena)}.')
    elif tam == 2 and unidade != 0:
        print(f'{escreve_dezenas(dezena)} e {escreve_unidades(unidade)}.')
    elif tam == 3 and dezena == 0 and unidade == 0:
        print(f'{escreve_centenas(centena)}.')
    elif tam == 3 and dezena == 0 and unidade != 0:
        print(f'{escreve_centenas(centena)} e {escreve_unidades(unidade)}.')
    elif tam == 3 and dezena != 0 and unidade == 0:
        print(f'{escreve_centenas(centena)} e {escreve_dezenas(dezena)}.')
    elif tam == 3 and dezena != 0 and unidade != 0:
        print(f'{escreve_centenas(centena)}, {escreve_dezenas(dezena)} e {escreve_unidades(unidade)}.')

def main():
    numero = int(input())

    if numero == 0:
        print('Valor inválido, número igual a zero')
    elif numero < 0:
        print('Valor inválido, número negativo')
    else:
        tamanho = tamanho_do_numero(numero)

        escrever_numero_por_extenso(numero, tamanho)

if __name__ == '__main__':
    main()