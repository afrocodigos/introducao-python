# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

from collections import Counter

def contar_frutas(lista_frutas):
    return Counter(lista_frutas)

def cria_frutas():
    lista_de_frutas = []

    while True:
        fruta = input("Digite o nome de uma fruta ou sair para terminar: ").strip().lower()

        if fruta.lower() == 'sair':
            break
        lista_de_frutas.append(fruta)

    return lista_de_frutas

lista_de_frutas = cria_frutas()
contagem = contar_frutas(lista_de_frutas)

print("Contagem das frutas:")
for fruta, quantidade in contagem.items():
    print(f"{fruta}: {quantidade}")
