# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

def ordenar_frutas(frutas):
    frutas.sort(key=str.lower)
    return frutas

frutas_fora_de_ordem = [
    "uva",
    "laranja",
    "abacaxi",
    "banana",
    "maçã",
    "manga",
    "limão",
    "pêssego",
    "morango",
    "melancia",
    "cereja",
    "kiwi",
    "abacate",
    "goiaba",
    "pera",
    "caqui",
    "figo",
    "carambola",
    "framboesa",
    "tangerina",
    "ameixa",
    "damasco",
    "jabuticaba",
    "acerola",
    "pitaya",
    "graviola"
]

frutas_ordenadas = ordenar_frutas(frutas_fora_de_ordem)

print ("Lista de frutas em ordem alfabética: ")
for fruta in frutas_ordenadas:
    print(fruta)