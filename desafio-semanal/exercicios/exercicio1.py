# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

lista_entrada = ["melancia","morango","limão","melancia","limão"]

lista_sem_duplicata_1 = list(set(lista_entrada))

print(f"Lista original: {lista_entrada}\n")
print("Método 1: Transformar a lista em set e depois retornar para uma lista")
print("Nesse método, a lista resultante aparecerá com componentes ordenados em ordem crescente")
print(f"Lista removendo as duplicatas transformando em set: {lista_sem_duplicata_1} \n")
