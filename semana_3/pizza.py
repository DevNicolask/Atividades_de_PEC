"""Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
quantas fatias cada um recebe e quantas sobram."""

quantidade_de_fatias = int(input("Quantas fatias tem essa pizza? "))
quantidade_de_amigos = int(input("Quantos amigos vão comer a pizza? "))
print(f'Cada amigo vai comer {quantidade_de_fatias//quantidade_de_amigos} fatias e vai sobrar {quantidade_de_fatias%quantidade_de_amigos} fatias.')
