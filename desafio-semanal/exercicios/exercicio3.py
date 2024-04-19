# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def lista_ordenada(lista):
    frutas_lista = list(set(lista))
    return frutas_lista
    
frutas = ["tamarindo", "maracujá", "Abacate", "Melão", "caju", "Banana", "Pêra"]
frutas_lista = frutas.sort(key=str.lower)
print(frutas)



