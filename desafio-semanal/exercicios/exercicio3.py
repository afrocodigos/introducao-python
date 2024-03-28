# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não:
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.


def order_list(list):
    return sorted(list)


fruit_list = ['melancia', 'cajá', 'morango', 'uva', 'jaca']
print(order_list(fruit_list))
