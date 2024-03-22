# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

lista_frutas = ['maça', 'banana', 'uva', 'caja', 'banana', 'manga', 'acerola', 'maça', 'banana']
lista_qtd_frutas = {} 

for i in lista_frutas:
    if i in lista_qtd_frutas:
        lista_qtd_frutas[i] += 1        
    else:
        lista_qtd_frutas[i] = 1
    
print(lista_qtd_frutas)

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.