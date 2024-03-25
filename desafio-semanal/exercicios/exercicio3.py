# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def ordenar_frutas(frutas):
    # Exibe a lista de frutas original
    print("Lista de frutas original:", end=" ")
    print(*frutas, sep=", ")
    
    # Ordena a lista de frutas em ordem alfabética
    frutas.sort(key=str.lower)
    
    # Exibe a lista de frutas ordenada
    print("\nLista de frutas ordenada:", end=" ")
    print(*frutas, sep=", ")

# Lista de frutas
frutas = ["Banana", "Maçã", "Uva", "Pera", "Laranja", "Limão", "Melancia", "Abacaxi", "Morango", "Manga"]

# Chama a função para ordenar a lista de frutas e exibir as listas
ordenar_frutas(frutas)
