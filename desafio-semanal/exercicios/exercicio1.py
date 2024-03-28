# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não:
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.


def remove_duplicates(duplicates_list):
    return list(set(duplicates_list))


duplicates_list = [9, 1, 2, 1, 5, 4, 3, 2, 5, 9, 10, 7, 8, 6, 6 ]
list_without_duplicates = remove_duplicates(duplicates_list)
print(list_without_duplicates)
