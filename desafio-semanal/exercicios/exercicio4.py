# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

fruits = ["pera", "uva", "Maça", "laranja", "pera", "Maça", "pera"]

def amount_fruits(list):
    dictionary = {}
    for fruit in list:
        if fruit in dictionary:
            dictionary[fruit] += 1
        else:
            dictionary[fruit] = 1
    return dictionary

print(amount_fruits(fruits))
