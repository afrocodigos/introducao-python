# Crie um programa que ordene uma lista de frutas em ordem alfabética.

lista_frutas = ['maça','laranja','tomate', 'uva', 'melancia', 'caqui', 'cajá']

lista_frutas.sort(key=str.lower)

print(lista_frutas)

    
# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.