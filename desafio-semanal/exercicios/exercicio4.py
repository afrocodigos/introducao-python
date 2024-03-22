# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

lista = ["Maça", "Uva", "Manga", "Abacate", "Tangerina", "Uva"]

conjunto = set(lista)
nova_lista = list(conjunto)

for fruta in (nova_lista):
  if lista.count(fruta) == 1:
    print(f"A fruta {fruta} aparece na lista apenas {lista.count(fruta)} vez.")
  else: 
    print(f"A fruta {fruta} aparece na lista {lista.count(fruta)} vezes.")