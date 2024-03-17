# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

lista = [1,2,3,4,5,2, "a", "a", "b"]

def remove_duplicidade_lista(lista):
    lista_sem_duplicidade = []
    for item in lista:
        if item not in lista_sem_duplicidade:
            lista_sem_duplicidade.append(item)
    return lista_sem_duplicidade

print(remove_duplicidade_lista(lista))