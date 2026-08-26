"""A fábrica de doces precisa de ajuda para embalar os doces corretamente. Cada pacote deve conter um número
inteiro de doces. Peça ao usuário para inserir o número de doces produzidos e o número de pacotes disponíveis.
Divida os doces igualmente entre os pacotes fazendo a divisão inteira para garantir que cada pacote contém a mesma
quantidade de doces. Imprima o número de doces em cada pacote."""

# Pergunta ao usuário quantos doces foram produzidos
numero_de_doces = int(input("Digite o número de doces produzidos: "))

# Pergunta ao usuário quantos pacotes estão disponíveis
numero_de_pacotes = int(input("Digite o número de pacotes disponíveis: "))

# Divide os doces igualmente entre os pacotes.
# O operador // realiza uma divisão inteira,
# garantindo que o resultado seja um número inteiro.
doces_por_pacote = numero_de_doces // numero_de_pacotes

# Exibe a quantidade de doces que ficará em cada pacote
print(f"Cada pacote terá {doces_por_pacote} doces.")
