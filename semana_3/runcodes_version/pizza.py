"""Faça um programa que pergunte ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostre
quantas fatias cada um recebe e quantas sobram."""

quantidade_de_fatias = int(input())
quantidade_de_amigos = int(input())
print(f'{quantidade_de_fatias//quantidade_de_amigos}\n{quantidade_de_fatias%quantidade_de_amigos}')
