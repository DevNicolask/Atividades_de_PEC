"""A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa Escreva um programa que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será a bonificação do funcionário."""

porcentagem = float(input("Digite a porcentagem do bônus (ex: 5 para 5%): "))
anos = float(input("Digite a quantidade de anos de serviço: "))
bonificação = float(anos * (porcentagem / 100))

print(f"O valor da bonificação é: {bonificação:.2f}")
