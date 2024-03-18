# AfroCódigos 2024
# Autora: Alfa Marine

# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Importa a função que capta a lista de entrada do usuário
from loop_func import loop_input


# Cria função para ordenar a lista em ordem crescente
def ordena_lista(lista_entrada):
    lista_saida = sorted(lista_entrada, key=str.lower)
    return lista_saida


# Testa a função de ordenar em ordem alfabética
lista_entrada_frutas = ["melancia","maçã","uva","banana",
                        "morango","limão","abacaxi"]
print("Por favor, insira sua lista de frutas")
lista_entrada_usuario = loop_input()

lista_ordenada_frutas = ordena_lista(lista_entrada_frutas)
lista_ordenada_usuario = ordena_lista(lista_entrada_usuario)

print()
print(f"Lista de frutas original: {lista_entrada_frutas}")
print(f"Lista de frutas ordenada: {lista_ordenada_frutas}")
print()
print(f"Lista do usuario original: {lista_entrada_usuario}")
print(f"Lista do usuario ordenada: {lista_ordenada_usuario}")
