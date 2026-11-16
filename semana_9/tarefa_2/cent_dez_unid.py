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


def numero_por_extenso(alg):
    numeros = {
        2: 'duas',
        3: 'tres',
        4: 'quatro',
        5: 'cinco',
        6: 'seis',
        7: 'sete',
        8: 'oito',
        9: 'nove'
    }

    return numeros.get(alg, '')


def escreve_unidades(algarismo):
    if algarismo == 1:
        return 'uma unidade'

    return numero_por_extenso(algarismo) + ' unidades'


def escreve_dezenas(algarismo):
    if algarismo == 1:
        return 'uma dezena'

    return numero_por_extenso(algarismo) + ' dezenas'


def escreve_centenas(algarismo):
    if algarismo == 1:
        return 'uma centena'

    return numero_por_extenso(algarismo) + ' centenas'


def escrever_numero_por_extenso(num):
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10

    partes = []

    if centena > 0:
        partes.append(escreve_centenas(centena))

    if dezena > 0:
        partes.append(escreve_dezenas(dezena))

    if unidade > 0:
        partes.append(escreve_unidades(unidade))

    if len(partes) == 1:
        resultado = partes[0]
    elif len(partes) == 2:
        resultado = ' e '.join(partes)
    else:
        resultado = ', '.join(partes[:-1]) + ' e ' + partes[-1]

    print(f"\nPor extenso: {num} = {resultado}.")


def main():
    print("--- Decomposição de Número por Extenso ---")
    numero = int(input("Digite um número inteiro positivo menor que 1000: "))

    if numero == 0:
        print('\nValor inválido: o número deve ser maior que zero.')
    elif numero < 0:
        print('\nValor inválido: não são permitidos números negativos.')
    elif numero >= 1000:
        print('\nValor inválido: o número deve ser menor que 1000.')
    else:
        escrever_numero_por_extenso(numero)


if __name__ == '__main__':
    main()