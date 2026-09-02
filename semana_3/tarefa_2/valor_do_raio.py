"""Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais."""

PI = 3.141592

raio = float(input("Digite o valor do raio: "))

comprimento = 2 * PI * raio
area_circulo = PI * (raio ** 2)
area_esfera = 4 * PI * (raio ** 2)
volume_esfera = (4 / 3) * PI * (raio ** 3)

print(f"Comprimento da circunferência: {comprimento:.6f}")
print(f"Área do círculo: {area_circulo:.6f}")
print(f"Área da esfera: {area_esfera:.6f}")
print(f"Volume da esfera: {volume_esfera:.6f}")