# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

lista_frutas = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra", "Uva", "Morango", "Morango", "Abacaxi"]

def contador(lista):
    dic_repetido = {}
    for i in lista:
        if i not in dic_repetido:
            dic_repetido[i] = 1
        else:
            dic_repetido[i] += 1
    print(dic_repetido)

contador(lista_frutas)