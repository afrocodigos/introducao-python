# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

def calculate_total_price(fruits):
    total = sum(fruits.values())
    return total


print("-"*10)
print("Vamos criar um catálogo de hortifruti, para isso insira frutas e seus valores "
    + "correspondentes. Ao finalizar, escreva 'sair' para ver a lista completa e o valor total")

frutas = {}
while True:
    fruta = input("Digite o nome da fruta: ")
    if fruta.lower() == 'sair':
        break
    preco = float(input("Digite o preço da fruta: "))
    frutas[fruta] = preco

preco_total = sum(frutas.values())

print("\nPreço total das frutas: ")
for fruta, preco in frutas:
    print(f"{fruta}: R${preco:.2f}")
    print(f"Total: R${preco_total:.2f}")