# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def duplicatas(lista):
    lista_sem_duplicidade = list(set(lista))
    return lista_sem_duplicidade

lista = [1, 23, 4, 5, 1, 4, 22, 23, 8, 9, 5, 9, 22]
lista_sem_duplicidade = duplicatas(lista)
print(lista_sem_duplicidade)
