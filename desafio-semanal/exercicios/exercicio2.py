# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

frutas = {"maça": 0, "pêra": 0, "laranja": 0, "melância": 0, "uva": 0}
total_frutas = 0

for fruta in frutas:
    preco = float(input(f"Digite o preço da {fruta} : "))
    frutas[fruta] = preco
    total_frutas += preco

print(f"O total é R${total_frutas}")