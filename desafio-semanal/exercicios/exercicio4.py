# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def contagem_frutas(lista):
    contador_frutas = {}

    for frutas in frutas_list:
        if frutas in contador_frutas:
            contador_frutas[frutas] += 1
        else:
            contador_frutas[frutas] = 1
    return contador_frutas

frutas_list = ["Abacate", "Pêra", "Uva", "Maçã", "Banana", "Pêra", "Melão", "Limão", "Uva", "Banana"]  
contador_frutas = frutas_list.sort() 
contagem = contagem_frutas(frutas_list)
      
for frutas, quantidade in contagem.items():
    print(f'{frutas}: {quantidade}')