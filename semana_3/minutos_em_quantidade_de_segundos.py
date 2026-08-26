"""O tempo é algo legal, especialmente quando você vai calcular quantos minutos há em um número específico de segundos. Peça ao usuário para inserir um número de segundos. Em seguida, use a divisão inteira para mostrar esse tempo em minutos (lembre-se, 1 minuto = 60 segundos) e use o resto da divisão inteira para saber quantos segundos sobram. Imprima os resultados"""

# Pergunta ao usuário o número de segundos
segundos = int(input("Digite o número de segundos: "))

# Exibe os minutos e os segundos restantes
print(f'Isso é igual a {int(segundos//60)} minutos e {int(segundos%60)} segundos.')
