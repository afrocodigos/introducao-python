# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

contagem_frutas = {}

def recebe_frutas():
    print("Insira a quantidade de frutas:")
    qtd = int(input())

    print("Agora insira as frutas:")
    frutas = []
    for i in range(0, qtd):
        frutas.append(input())
    return frutas

frutas = recebe_frutas()

for fruta in frutas:
  contagem_frutas[fruta] = contagem_frutas.get(fruta, 0) + 1

for fruta, contagem in contagem_frutas.items():
  print(f"A fruta '{fruta}' aparece {contagem} vezes.")
