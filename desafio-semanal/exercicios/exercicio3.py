# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def cria_lista():
    lista_de_frutas = [] 
    
    while True:
        fruta = input("Digite o nome de uma fruta, ou sair para terminar o programa: ").strip().lower()
        
        if fruta.lower() == 'sair':
            break
        
        lista_de_frutas.append(fruta)
        lista_de_frutas.sort()
    
    return lista_de_frutas

frutas = cria_lista()

print("A lista de frutas é:", frutas)