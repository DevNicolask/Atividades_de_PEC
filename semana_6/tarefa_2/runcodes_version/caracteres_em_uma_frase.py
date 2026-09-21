"""
Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa frase sem considerar espaços em branco no início ou final da frase digitada.
"""
def tamanho(string):
    tamanho_string = len(string)
    return tamanho_string

def main():
    frase = input().strip()

    print(tamanho(frase))

if __name__ == '__main__':
    main()