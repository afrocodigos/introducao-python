# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

# Exemplo de lista com duplicatas
list = [1, 2, 2, 10, 4, 5, 1, 1, 13, 13, 15]

listNotDuplicate = []

for elemento in list:
    if elemento not in listNotDuplicate:
        listNotDuplicate.append(elemento)


print(listNotDuplicate)