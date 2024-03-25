# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.


frutas = ['Banana', 'Maçã', 'Pera', 'Banana', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera', 'Banana', 'Maçã', 'Uva', 'Morango', 'Banana', 'Maçã', 'Pera', 'Uva', 'Laranja', 'Pera']

thisset=set((frutas))
listadefrutas=[]
for i in thisset:
    listadefrutas.append(i)
print(listadefrutas)