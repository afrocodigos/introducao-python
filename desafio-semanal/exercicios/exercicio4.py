# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.
#Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.
lista_frutas = []
cont = 0
tamanho_lista = int(input("Quantidade de frutas: "))
for umaChave in range(tamanho_lista):
    frutas = str(input("Nome de fruta: "))
    lista_frutas.append(frutas)

print(lista_frutas)

for umaChave2 in lista_frutas:
    contagem = lista_frutas.count(umaChave2)
    if contagem > 1:
        print(f"A fruta {umaChave2} aparece {contagem} vezes. ")


