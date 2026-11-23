"""
Leia as notas de 50 alunos.
Mostre uma lista com os índices dos alunos que possuem nota
maior ou igual a 6.
"""

def verifica_notas(LISTA):
    INDICES = []

    for i in range(len(LISTA)):
        if LISTA[i] >= 6:
            INDICES.append(i)

    return INDICES


def main():
    NOTAS = [float(input()) for _ in range(50)]

    RESULTADO = verifica_notas(NOTAS)

    print(RESULTADO)


if __name__ == "__main__":
    main()