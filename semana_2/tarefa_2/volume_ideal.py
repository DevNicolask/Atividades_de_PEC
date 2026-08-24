"""Desenvolva um programa que peça ao usuário o nível de volume atual e o nível de volume desejado de seu aparelho
de som. Calcule e mostre a diferença de volume necessária."""

volume_atual = int(input('Qual o volume que você está atualmente? '))
volume_ideal = int(input('Qual é o volume ideal? '))

print(f'A diferença de volume necessária é: {volume_ideal - volume_atual}')
