"""Pergunte ao usuário quantos quilômetros até Marte e quantos quilômetros por hora sua nave espacial pode viajar.
Calcule e mostre quanto tempo levaria para chegar a Marte."""

km_ate_marte = float(input('Qual a distância até marte em Km? '))
velocidade_em_km_por_hora = float(input('Qual a sua velocidade em Km/h? '))

print(f'Então você chegará a marte em {km_ate_marte/velocidade_em_km_por_hora:.2} horas.')
