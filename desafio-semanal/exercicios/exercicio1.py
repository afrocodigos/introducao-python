# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

def duplicate_remover(list_input):
    unduplicated_list = list(set(list_input))
    ordened_unduplicated_list = sorted(unduplicated_list)
    return (f"lista sem valores duplicados: {ordened_unduplicated_list}")

print("-"*100)
print("Vamos testar a função de remoção de valores duplicados. Para isso preciso que você insira numeros inteiros na seguinte lista.")

numbers_list = []
counter = 0
while counter < 10:
    user_input = int(input(f"Por favor, insira o {counter + 1}º número: "))
    try:
        number = int(user_input)
        numbers_list.append(number)
        counter += 1
    except ValueError:
        print("Por favor, insira um número válido.")

print("Os números inseridos são:", numbers_list)
print(duplicate_remover(numbers_list))
