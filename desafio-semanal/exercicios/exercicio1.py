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

# Serão criados duas funções para a remoção de duplicatas
# Função 1
def remove_duplicata_1(lista_entrada):
  return list(set(lista_entrada))

# Função 2
def remove_duplicata_2(lista_entrada):
  lista_saida = []
  lista_duplicatas = []

  for elemento in lista_entrada:
    if elemento in lista_saida:
      lista_duplicatas.append(elemento)
    else:
      lista_saida.append(elemento)

  return lista_saida

