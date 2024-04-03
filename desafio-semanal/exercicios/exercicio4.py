# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = ["maça", "laranja", "limão", "pêra", "abaxaci", "melância", "carambola", "maça", "laranja", "laranja"]

ocorrencia_frutas = dict()

for fruta in frutas:
    if fruta not in ocorrencia_frutas:
        ocorrencia_frutas[fruta] = 1
    else:
        ocorrencia_frutas[fruta] += 1

print(ocorrencia_frutas)