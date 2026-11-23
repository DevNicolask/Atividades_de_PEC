"""
Escreva um programa que leia um número n. Considere uma lista com n posições, e então: 

a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro) casas decimais.

b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa decimal.

c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
"""

def main():
    n = int(input())

    # A) Valores reais na ordem inversa
    valores = [float(input()) for _ in range(n)]
    valores.reverse()
    print([] if n == 0 else [round(valor, 4) for valor in valores])

    # B) Notas e média
    notas = [float(input()) for _ in range(n)]
    print([round(nota, 1) for nota in notas])
    if n != 0:
        media = sum(notas) / n

        print(f"{media:.1f}")
    else:
        print("SEM NOTAS")

    # C) Contagem de vogais e impressão das consoantes
    letras = [input().strip() for _ in range(n)]

    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    quantidade_vogais = sum(1 for letra in letras if letra in vogais)
    consoantes = [letra for letra in letras if letra not in vogais]

    print(quantidade_vogais)
    print(consoantes)


if __name__ == "__main__":
    main()