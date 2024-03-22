# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

frutas = ["Maçã", "Uva", "Pera", "Manga", "Limão", "Abacaxi", "Cupuaçu", "Limão", "Abacaxi", "Cupuaçu", "Limão", "Uva", "Pera", "Manga","Uva", "Pera", "Manga",]
chaves = set(frutas)
chaves
for chave in chaves:
    print(f'A fruta {chave} está presente {frutas.count(chave)} vezes.')