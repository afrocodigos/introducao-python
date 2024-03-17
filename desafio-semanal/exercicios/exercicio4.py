# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = ["limão", "banana", "uva", "limão", "laranja", "uva", "maçã", "abacaxi", "uva", "Pera", "limão", "uva", "melão","maçã", "laranja", "laranja", "uva", "abacaxi", "limão"]

contagem_frutas = {}

for fruta in frutas:
    if fruta in contagem_frutas:
        contagem_frutas[fruta] += 1
    else:
        contagem_frutas[fruta] = 1

print("Contagem de frutas:", contagem_frutas)

