# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

## Sort()
# Método utilizado para modificar a lista original e não precisar da lista original.)
lista_frutas = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

lista_frutas.sort(key=str.lower)

print("Sort: ", lista_frutas)

## Sorted()
# Use sorted() quando precisar manter a lista original inalterada ou quando estiver trabalhando 
# com qualquer iterável, não apenas listas, e quiser uma nova lista ordenada como resultado.)

lista_frutas_2 = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

lista_frutas_ordenada = sorted(lista_frutas_2)

print("Sorted: ", lista_frutas_ordenada)

## Bubble Sort (Algoritmo de ordenação)

# 1. Comece no início da lista.
# 2. Compare os dois primeiros elementos.
# 3. Se o primeiro elemento for maior que o segundo, troque-os de lugar.
# 4. Mova para os próximos elementos, do início ao fim.
# 5. Continue até que uma passagem completa seja feita sem nenhuma troca, indicando que a lista está ordenada.

lista_frutas_3 = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

bubble_sort(lista_frutas_3)

print("Bubble Sort: ", lista_frutas_3)