#Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def remover_duplicatas(lista):
    # Convertendo a lista para um conjunto para remover as duplicatas
    conjunto_sem_duplicatas = set(lista)
    # Convertendo o conjunto de volta para uma lista
    lista_sem_duplicatas = list(conjunto_sem_duplicatas)
    return lista_sem_duplicatas

# Lista original com duplicatas
lista_original = [1, 2, 3, 4, 2, 3, 5, 6, 1, 7, 8, 9, 5,10, 20, 30, 20, 40, 50, 10, 60, 70, 80, 90, 40, 100]

# Removendo as duplicatas da lista original
lista_sem_duplicatas = remover_duplicatas(lista_original)

# Imprimindo a lista resultante
print("Lista original:", lista_original)
print("Lista sem duplicatas:", lista_sem_duplicatas)
