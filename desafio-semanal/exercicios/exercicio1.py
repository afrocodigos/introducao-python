# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

import random
# Criando uma lista com números sortidos e duplicatas usando o operador de multiplicação e shuffle

def criar_lista_com_duplicatas(tamanho, duplicata):
    numeros_ordenados = list(range(tamanho))
    lista_com_duplicatas = [random.choice(numeros_ordenados) for _ in range(duplicata)] * tamanho
    random.shuffle(lista_com_duplicatas)
    return lista_com_duplicatas

tamanho = 15
duplicata = 5
resultado = criar_lista_com_duplicatas(tamanho, duplicata)

def remover_duplicatas(resultado):  
    lista_sem_duplicatas = []
    for elemento in resultado:
        if elemento not in lista_sem_duplicatas:
            lista_sem_duplicatas.append(elemento)
    return lista_sem_duplicatas

resultado_sem_duplicata = remover_duplicatas(resultado)

print("Esta é a nossa lista!")
print()
print(resultado)
print()
print("Eliminamos as duplicatas =D")
print()
print(resultado_sem_duplicata)