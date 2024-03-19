# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

lista = [6,1, 2, 3, 4, 2, 3, 5, 6, 4,7,7,9,8,9]

lista_sem_duplicatas = list(set(lista))

print("Lista sem duplicatas:", lista_sem_duplicatas)
