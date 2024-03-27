# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Primeiro atribuí uma variavel para minha lista com duplicatas
lista_com_duplicatas = [1,2,2,3,3,3,4,5,5,6,7,7]
#Em seguida, converti minha lista com duplicatas, usando o set,  que irá remover as duplicadas.
set_sem_duplicadas = set(lista_com_duplicatas)
#Logo, tranformei o conjunto set para um conjunto em lista.
lista_sem_duplicatas = list(set_sem_duplicadas)
print(f"A lista sem duplicatas:{ lista_sem_duplicatas}")