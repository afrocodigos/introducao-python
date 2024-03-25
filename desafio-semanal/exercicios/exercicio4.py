# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = [
    "maçã", "banana", "laranja", "maçã", "uva",
    "banana", "maçã", "uva", "laranja", "maçã",
    "morango", "abacaxi", "pera", "abacate", "limão",
    "manga", "goiaba", "caqui", "cereja", "kiwi",
    "abacaxi", "laranja", "morango", "banana", "maçã",
    "pêssego", "ameixa", "melancia", "pêra", "figo",
    "carambola", "framboesa", "tangerina", "jabuticaba",
    "acerola", "pitaya", "graviola", "abacate", "goiaba",
    "damasco", "kiwi", "cereja", "abacaxi", "melancia",
    "maçã", "banana", "laranja", "maçã", "uva",
    "banana", "maçã", "uva", "laranja", "maçã",
    "morango", "abacaxi", "pera", "abacate", "limão",
    "manga", "goiaba", "caqui", "cereja", "kiwi",
    "abacaxi", "laranja", "morango", "banana", "maçã",
    "pêssego", "ameixa", "melancia", "pêra", "figo",
    "carambola", "framboesa", "tangerina", "jabuticaba",
    "acerola", "pitaya", "graviola", "abacate", "goiaba",
    "damasco", "kiwi", "cereja", "abacaxi", "melancia"
]

contagem_frutas = {}

for fruta in frutas:
    if fruta in contagem_frutas:
        contagem_frutas[fruta] += 1
    else:
        contagem_frutas[fruta] = 1

print("Contagem de frutas:")

for fruta, quantidade in contagem_frutas.items():
    print(f"{fruta}: {quantidade}")