"""
Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

a) "Telefonou para a vítima?"
b) "Esteve no local do crime?"
c) "Mora perto da vítima?"
d) "Devia para a vítima?"
e) "Já trabalhou com a vítima?"

Considere “S” para sim ou “N” para não. O programa deve emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

def quantos_sim(resp1, resp2, resp3, resp4, resp5):
    quantidade = 0

    if resp1 == "S":
        quantidade += 1

    if resp2 == "S":
        quantidade += 1

    if resp3 == "S":
        quantidade += 1

    if resp4 == "S":
        quantidade += 1

    if resp5 == "S":
        quantidade += 1 

    return quantidade

def analise(quantidade_sim):
    if quantidade_sim == 2:
        return "Suspeito"
    
    elif 3 <= quantidade_sim <= 4:
        return "Cúmplice"
    
    elif quantidade_sim == 5:
        return "Assassino"
    
    else:
        return "Inocente"

def main():
    print("--- Interrogatório Investigativo ---")
    print("Responda às perguntas abaixo com 'S' para Sim ou 'N' para Não:\n")
    
    resposta_1 = input("1. Telefonou para a vítima? (S/N): ").strip().upper()
    resposta_2 = input("2. Esteve no local do crime? (S/N): ").strip().upper()
    resposta_3 = input("3. Mora perto da vítima? (S/N): ").strip().upper()
    resposta_4 = input("4. Devia para a vítima? (S/N): ").strip().upper()
    resposta_5 = input("5. Já trabalhou com a vítima? (S/N): ").strip().upper()

    q_sim = quantos_sim(resposta_1, resposta_2, resposta_3, resposta_4, resposta_5)

    classificacao = analise(q_sim)

    print(f"\nClassificação do entrevistado: {classificacao}")

if __name__ == '__main__':
    main()