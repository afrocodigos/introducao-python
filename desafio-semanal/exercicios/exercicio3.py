# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

# Respondido por Lucas Teles.

def lista_ordenada(lista):
    frutas_lista = list(set(lista))
    return frutas_lista
    
frutas = ["Uva", "Cajá", "Abacate", "Melão", "Açai", "Banana", "Melancia"]
frutas_lista = frutas.sort(key=str.lower)
print(frutas)