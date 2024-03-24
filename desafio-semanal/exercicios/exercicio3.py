# Crie um programa que ordene uma lista de frutas em ordem alfabética.

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