# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def ordenar_frutas(lista_frutas):
    lista_frutas.sort(key=str.lower)  # Ordena a lista em ordem alfabética 
    return lista_frutas

# Lista de frutas
frutas = ["Caju", "Mangava", "Bocaiuva","pequi", "Araticum", "Jatobá", "Pequi","Acerola"]

# Chama a função para ordenar as frutas
frutas_ordenadas = ordenar_frutas(frutas)

# Imprime as frutas ordenadas
print("Frutas ordenadas:")
for fruta in frutas_ordenadas:
    print(fruta)

    