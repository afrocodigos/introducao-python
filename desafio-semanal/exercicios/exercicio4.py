# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def contar_frutas(lista_frutas):

  dicionario = {}
  for fruta in lista_frutas:
    if fruta in dicionario:
      dicionario[fruta] += 1
    else:
      dicionario[fruta] = 1
  return dicionario

lista_frutas = ["maçã", "banana", "laranja", "maçã", "abacaxi", "banana"]

dicionario_frutas = contar_frutas(lista_frutas)

for fruta, quantidade in dicionario_frutas.items():
  print(f"{fruta}: {quantidade}")