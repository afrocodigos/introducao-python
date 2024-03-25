# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def contar_frutas(frutas):
    # Exibe a lista de frutas original
    print("Lista de frutas:", end=" ")
    print(*frutas, sep=", ")
    
    # Conta a quantidade de ocorrências de cada fruta
    contagem_frutas = {}
    for fruta in frutas:
        if fruta in contagem_frutas:
            contagem_frutas[fruta] += 1
        else:
            contagem_frutas[fruta] = 1
    
    # Exibe a quantidade de ocorrências de cada fruta
    print("\nContagem de frutas:")
    for fruta, contagem in contagem_frutas.items():
        print(f"{fruta}: {contagem}")

# Lista de frutas
frutas = ["Banana", "Maçã", "Uva", "Pera", "Laranja", "Limão", "Melancia", "Abacaxi", "Morango", "Manga", "Banana", "Maçã", "Uva", "Pera", "Laranja", "Limão", "Melancia", "Abacaxi", "Morango", "Manga", "Banana", "Maçã", "Uva", "Pera", "Laranja", "Limão", "Melancia", "Abacaxi", "Morango", "Manga"]

# Chama a função para contar as frutas e exibir a contagem
contar_frutas(frutas)
