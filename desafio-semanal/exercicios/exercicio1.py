# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

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

def remove_duplicatas(lista_frutas): 
    lista_final = list(set(lista_frutas))
    lista_final.sort()

    return lista_final

lista_final = remove_duplicatas(frutas)

print("Lista com todas as frutas: ", frutas)
print("Lista de frutas sem nomes duplicados: ", lista_final)