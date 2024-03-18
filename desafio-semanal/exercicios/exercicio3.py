# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

## Sort()
# Método utilizado para modificar a lista original e não precisar da lista original.)
lista_frutas = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

lista_frutas.sort()

print("Sort", lista_frutas)

## Sorted()
# Use sorted() quando precisar manter a lista original inalterada ou quando estiver trabalhando 
# com qualquer iterável, não apenas listas, e quiser uma nova lista ordenada como resultado.)

lista_frutas_2 = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

lista_frutas_ordenada = sorted(lista_frutas_2)

print("Sorted: ", lista_frutas_ordenada)

## Bubble Sort

# Comece no início da lista: Compare os dois primeiros elementos (elemento 0 e elemento 1).

# Compare e troque (se necessário): Se o primeiro elemento for maior que o segundo (considerando a ordenação ascendente), troque-os de lugar.

# Mova para os próximos elementos: Repita o processo de comparação e troca para cada par de elementos adjacentes na lista, do início ao fim. Isso completa uma "passagem" pela lista.

# Repita até ordenado: Ao final de cada passagem, o maior elemento "borbulha" até o final da lista, assumindo sua posição correta. Repita as passagens pela lista, excluindo o final de cada vez, pois os maiores elementos já estarão em suas posições corretas. Continue até que uma passagem completa seja feita sem nenhuma troca, indicando que a lista está ordenada.

lista_frutas_3 = ["Morango", "Abacaxi", "Uva", "Mamão", "Banana", "Maçã", "Pêra"]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

bubble_sort(lista_frutas_3)

print("Bubble Sort: ", lista_frutas_3)