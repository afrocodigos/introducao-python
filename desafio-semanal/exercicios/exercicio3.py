# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

#Resposta

def order_fruits (fruit_list):
  fruit_list.sort(key=str.lower)
  return fruit_list

fruits = ["Manga", "Mamão", "Caqui", "Abacaxi", "Abacate", "Jabuticaba", "Limão", "Laranja", "Graviola"]
fruits_order = order_fruits(fruits)
print(f"Ordem alfabética das frutas: {fruits_order}")