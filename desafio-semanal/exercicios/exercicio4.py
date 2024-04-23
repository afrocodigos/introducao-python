#Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

def contar_frutas(lista_frutas):
    contagem_frutas = {}  # Dicionário para armazenar a contagem de cada fruta
    
    # Passa pela lista e incrementa o valor do dicionário para cada fruta encontrada
    for fruta in lista_frutas:
        fruta = fruta.lower()
        if fruta in contagem_frutas:
            contagem_frutas[fruta] += 1
        else:
            contagem_frutas[fruta] = 1
    
    return contagem_frutas

# Lista de frutas
frutas = ["Caju", "Mangava", "Bocaiuva","pequi","Manga","bocaiuva", "Araticum", "Caju","Jatobá", "Pequi","Acerola"]
# Chama a função para contar as frutas
contagem = contar_frutas(frutas)

# Imprime o dicionário com a contagem de frutas
print("Contagem de frutas:")
for fruta, quantidade in contagem.items():
    print(f"{fruta}: {quantidade}")
