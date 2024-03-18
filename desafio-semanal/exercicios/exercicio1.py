# AfroCódigos 2024
# Autora: Alfa Marine

# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Importa a função que capta a lista de entrada do usuário
from loop_func import loop_input


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


# Testando as funções
lista_entrada_numeros = [1,6,3,5,4,2,5,1,4,5]
lista_entrada_frutas = ["melancia","maçã","uva","melancia",
                        "banana","morango","banana","uva",
                        "melancia","maçã","limão","abacaxi"]
print("Por favor, insira sua lista")
lista_entrada_usuario = loop_input()

print()
print("Método 1: Transforma a lista em set e depois retorna para uma lista")
print("Método 2: Copia o valor de um item da lista para a lista de saída caso o valor do item não tiver sido inserido antes")

lista_saida_frutas_1 = remove_duplicata_1(lista_entrada_frutas)
lista_saida_frutas_2 = remove_duplicata_2(lista_entrada_frutas)

print()
print(f"Lista de frutas original: {lista_entrada_frutas}")
print(f"Lista removendo as duplicatas com o método 1: {lista_saida_frutas_1}")
print(f"Lista removendo as duplicatas com o método 2: {lista_saida_frutas_2}")

lista_saida_numeros_1 = remove_duplicata_1(lista_entrada_numeros)
lista_saida_numeros_2 = remove_duplicata_2(lista_entrada_numeros)

print()
print(f"Lista de números original: {lista_entrada_numeros}")
print(f"Lista removendo as duplicatas com o método 1: {lista_saida_numeros_1}")
print(f"Lista removendo as duplicatas com o método 2: {lista_saida_numeros_2}")

lista_saida_usuario_1 = remove_duplicata_1(lista_entrada_usuario)
lista_saida_usuario_2 = remove_duplicata_2(lista_entrada_usuario)

print()
print(f"Lista do usuário original: {lista_entrada_usuario}")
print(f"Lista removendo as duplicatas com o método 1: {lista_saida_usuario_1}")
print(f"Lista removendo as duplicatas com o método 2: {lista_saida_usuario_2}")
