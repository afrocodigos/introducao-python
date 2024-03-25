# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def alphabetical_order(fruits_list):
    fruits_list.sort(key=str.lower)
    return (f"lista de frutas sem duplicados: {fruits_list}")

# fruits_list = frutas = ["Banana", "Maçã", "Abacaxi", "Uva", "Pêssego", "Laranja"]
fruits_list = []
counter = 0

while True:
    user_input = input("Digite o nome da fruta ou sair para finalizar: ")
    if user_input.lower() == "sair":
        break
    fruit = user_input
    fruits_list.append(fruit)
    counter += 1

print (alphabetical_order(fruits_list))