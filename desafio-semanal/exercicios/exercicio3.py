# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

list = ['goiba', 'acerola', 'banana', 'caja']

list.sort(key=str.lower) 

print(list)