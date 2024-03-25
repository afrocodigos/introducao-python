# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def remover_duplicatas(lista):
    # Exibir a lista original
    print("Lista inicial:", end=" ")
    print(*lista, sep=", ")

    # Remover duplicatas da lista
    lista_sem_duplicatas = list(set(lista))

    # Exibir a lista sem duplicatas
    print("\nLista sem duplicatas:", end=" ")
    print(*lista_sem_duplicatas, sep=", ")

# Lista original
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Chamar a função para remover duplicatas e exibir as listas
remover_duplicatas(lista)
