"""
Leia uma quantidade n, seguida de uma lista com n valores.
Imprima LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
"""

def esta_ordenado(LISTA):
    for i in range(len(LISTA) - 1):
        if LISTA[i] > LISTA[i + 1]:
            return False

    return True


def main():
    try:
        n = int(input())
        LISTA = []
        
        for _ in range(n):
            valor = float(input())
            LISTA.append(valor)

        if esta_ordenado(LISTA):
            print("LISTA ORDENADA")
        else:
            print("LISTA NÃO ORDENADA")

    except ValueError:
        print("LISTA NÃO ORDENADA")
        return


if __name__ == "__main__":
    main()