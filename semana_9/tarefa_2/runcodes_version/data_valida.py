"""
Escreva um programa que leia uma data no formado DDMMAAA e informe se é uma data válida.

OBS: Use apenas condicionais e os tipos básicos do Python; Não utilize bibliotecas do Python que tratam datas; Considere que em anos bissextos o mês de fevereiro tem 29 dias.
"""

def ano_bissexto(ano_teste):
    if ano_teste % 4 == 0 and ano_teste %  100 == 0 and ano_teste % 400 == 0:
        return True
    
    elif ano_teste % 4 == 0 and ano_teste %  100 == 0:
        return False
    
    elif ano_teste % 4 == 0:
        return True
    
    else:
        return False

def validar_dia(valor_dia, valor_mes, valor_ano):
    if valor_mes in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= valor_dia <= 31
    
    elif valor_mes in [4, 6, 9, 11]:
        return 1 <= valor_dia <= 30
    
    elif valor_mes == 2:
        if ano_bissexto(valor_ano):
            return 1 <= valor_dia <= 29
        else:
            return 1 <= valor_dia <= 28
    else:
        return False

def validar_mes(valor_mes):
    return 1 <= valor_mes <= 12

def validar_ano(valor_ano):
    return valor_ano >= 1

def validar(dia, mes, ano):
    resultado_da_analise = validar_dia(dia, mes, ano) and validar_mes(mes) and validar_ano(ano)
    return resultado_da_analise

def main():
    data = input()

    dd = data[0:2]
    mm = data[2:4]
    aaaa = data[4:8]

    print(validar(int(dd), int(mm), int(aaaa)))

if __name__ == '__main__':
    main()