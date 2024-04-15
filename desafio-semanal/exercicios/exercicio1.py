# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

# Implementação:

# Lista com duplicatas
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
new_list = list(set(lista))
print(new_list) # [1, 2, 3, 4, 5]