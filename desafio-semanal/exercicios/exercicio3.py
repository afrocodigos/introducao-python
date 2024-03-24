# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def recebe_frutas():
    print("Insira a quantidade de frutas:")
    qtd = int(input())

    print("Agora insira as frutas:")
    frutas = []
    for i in range(0, qtd):
        frutas.append(input())
    return frutas

def ordena_frutas(frutas):
    frutas.sort(key=str.lower)
    return frutas

print(ordena_frutas(recebe_frutas()))