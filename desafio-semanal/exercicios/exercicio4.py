# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

repeatedFruits = ["maçã", "banana", "laranja", "uva", "morango", "banana", "maçã", "laranja"]


frutsCount = {}

for fruta in repeatedFruits:
    if fruta in frutsCount:
        frutsCount[fruta] += 1
    else:
        frutsCount[fruta] = 1


print(frutsCount)