"""Desenvolva um programa que pergunte a distância até um planeta em quilômetros e a velocidade da nave em km/h.
Informe quantos dias e quantas horas a viagem levará, considerando 24 horas por dia."""

distancia_ate_um_planeta = float(input()) # Distância em Km
velocidade_da_nave = float(input()) # Velocidade Média em Km/h
tempo_da_viagem = distancia_ate_um_planeta/velocidade_da_nave # Tempo em horas 

print(f'{int(tempo_da_viagem//24)} dias e {int(tempo_da_viagem%24)} horas')
