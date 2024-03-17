# AfroCódigos 2024
# Autora: Alfa Marine

# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def remove_duplicata(lista_entrada):
  lista_saida = []
  lista_duplicatas = []

  for elemento in lista_entrada:
    if elemento in lista_saida:
      lista_duplicatas.append(elemento)
    else:
      lista_saida.append(elemento)

  return lista_saida

def ordena_lista(lista_entrada):
    lista_saida = sorted(lista_entrada, key=str.lower)
    return lista_saida

def conta_frutas(lista_frutas):    
    frutas = remove_duplicata(lista_frutas)
    frutas_ordenadas = ordena_lista(frutas)
    dict_frutas = {}

    for fruta in frutas_ordenadas:
        dict_frutas[fruta] = lista_frutas.count(fruta)

    return dict_frutas


lista_entrada_frutas = ["melancia","maçã","uva","melancia",
                        "banana","morango","banana","uva",
                        "melancia","maçã","limão","abacaxi"]
dict_quantidade_frutas = conta_frutas(lista_entrada_frutas)

print(dict_quantidade_frutas)