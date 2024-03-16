# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

lista_entrada = [1,2,6,3,7,4,2,1,6,2]

lista_sem_duplicata = list(set(lista_entrada))

print(f"Lista original: {lista_entrada}")
print(f"Lista removendo as duplicatas: {lista_sem_duplicata}")
