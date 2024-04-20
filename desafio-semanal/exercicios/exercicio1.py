# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

lista = [9, 8, 1, 3, 5, 8, 2, 6, 4, 9, 7, 3]

lista.sort()

lista_2 = [lista[i] for i in range(len(lista)-1) if lista[i] != lista[i+1]]
lista_2.append(lista[-1])

print(lista_2)

