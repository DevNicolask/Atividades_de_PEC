"""
Leia um número n e considere uma lista com n posições.

a) Leia valores reais e imprima a lista na ordem inversa,
considerando até 4 casas decimais.

b) Leia n notas, imprima as notas e a média,
considerando 1 casa decimal.

c) Leia n letras, conte as vogais e imprima as consoantes.
"""

def main():
    n = int(input())

    # A) Valores reais na ordem inversa
    valores = [float(input()) for _ in range(n)]
    valores.reverse()
    print([round(valor, 4) for valor in valores])

    # B) Notas e média
    notas = [float(input()) for _ in range(n)]
    media = sum(notas) / n

    print([round(nota, 1) for nota in notas])
    print(f"{media:.1f}")

    # C) Contagem de vogais e impressão das consoantes
    letras = [input().strip() for _ in range(n)]

    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    quantidade_vogais = sum(1 for letra in letras if letra in vogais)
    consoantes = [letra for letra in letras if letra not in vogais]

    print(quantidade_vogais)
    print(consoantes)


if __name__ == "__main__":
    main()