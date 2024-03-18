# AfroCódigos 2024
# Autora: Alfa Marine

# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Importa a função que capta a lista de entrada do usuário
from loop_func import loop_input


# Cria função para calcular o preço total
def calcula_preco_total(lista_precos):
    preco_total = 0

    for preco in lista_precos:
        preco_total += preco

    return preco_total


# Testa a função calcula_preco_total
print("Por favor, insira o preço de cada fruta")
precos_frutas = loop_input()
precos_frutas = [float(preco_fruta) for preco_fruta in precos_frutas]
preco_total_frutas = calcula_preco_total(precos_frutas)

print()
print(f"Preço total das frutas: R$ {preco_total_frutas}")

