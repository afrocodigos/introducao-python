# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.
lista_frutas = []
tamanho_da_lista = int(input("Digite a quantidade de frutas"))
for umaChave in range(tamanho_da_lista):
    fruta = str(input("Digite a fruta: "))
    lista_frutas.append(fruta)
lista_frutas.sort()
print(lista_frutas)