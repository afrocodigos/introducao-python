# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Criei uma lista de frutas
lista_frutas = ["acerola", "manga", "uva", "jabuticaba", "melão", "melão", "uva", "uva", "laranja"]

# Logo, crie um dicionário para armazenar o número de vezes que cada fruta aparece.
contagem_frutas = {}

# Passei pela lista e incrementei o valor do dicionário para cada fruta encontrada
for fruta in lista_frutas:
    # Verifiquei se a fruta já está no dicionário
    if fruta in contagem_frutas:
        contagem_frutas[fruta] += 1
    else:
        # Se não estiver, adiciona a fruta ao dicionário com valor 1
        contagem_frutas[fruta] = 1

# Imprimi o dicionário de contagem de frutas
print("Contagem de frutas:", contagem_frutas)
