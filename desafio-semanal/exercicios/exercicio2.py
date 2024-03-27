# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

frutas = {}

while True: 
    nome_fruta = input("Insira o nome da fruta, ou total para calcular o valor total das frutas:")

    if nome_fruta.lower() == "total": 
        break
    
    preco_fruta = float(input(f"Insira o preço da fruta {nome_fruta}:"))
    frutas[nome_fruta] = preco_fruta


preco_total = sum(frutas.values())

print(f"Preço total de todas as frutas: R${preco_total: .2f}")

    