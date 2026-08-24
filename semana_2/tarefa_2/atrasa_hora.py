"""Você já se perguntou como seria um relógio que atrasa 3 minutos a cada hora? Vamos modelar isso com
programação! Peça ao usuário para inserir o número de horas. Calcule e imprima o tempo que um relógio que atrasa
3 minutos por hora estaria atrás."""

hora = int(input('Quantas horas se passou? '))
hora_atrasada = hora * 3
print(f'Então o relógio que atrasa 3 minutos a cada hora já atrasou {hora_atrasada} minutos.')
