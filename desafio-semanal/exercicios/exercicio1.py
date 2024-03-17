# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.


lista_nome1 = ["nome1","nome2","nome3"]
lista_nome2 = ["nome1","nome4","nome5"]

lista_juntas = set(lista_nome1+lista_nome2)#a estrutura set garante que os dados só iram ser mostrado uma vez
lista_juntadas = list(lista_juntas)

print(lista_juntadas)