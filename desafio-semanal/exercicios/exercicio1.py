# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

tooDo = []

while True:
    elemento = input("Digite um elemento para a lista (ou digite 'sair' para finalizar): ")
    if elemento == "sair":
        break
    else:
        tooDo.append(elemento)
    print(tooDo)
    newToodo=list(dict.fromkeys(tooDo))
    print(newToodo)