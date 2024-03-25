# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def count_fruits(fruits_list):
    fruit_counts = {}

    for fruit in fruits_list:
        if fruit in fruit_counts:
            fruit_counts[fruit] += 1
        else:
            fruit_counts[fruit] = 1

    return fruit_counts

fruits_list = []

while True:
    user_input = input("Digite o nome da fruta ou 'sair' para finalizar: ")
    if user_input.lower() == "sair":
        break
    fruits_list.append(user_input)

fruit_counts = count_fruits(fruits_list)

print("Contagem de frutas:")
for fruit, count in fruit_counts:
    print(f"{fruit}: {count}")
