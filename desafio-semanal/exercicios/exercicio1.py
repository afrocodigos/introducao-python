# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.


#entrada dos dados
lista = [1,1,2,2,3,3,4,4,5,5]

eliminar_duplicatas = set(lista)
    
print(eliminar_duplicatas)
    
# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.