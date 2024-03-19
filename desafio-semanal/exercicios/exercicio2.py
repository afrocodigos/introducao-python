# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

preco_total = 0

num_frutas = int(input("Quantas fruntas você deseja inserir? "))

for i in range(num_frutas):
    nome_fruta = input("Digite o nome da fruta: ")
    preco_fruta = float(input(f"Digite o preço da fruta {nome_fruta}: "))
    preco_total += preco_fruta

print("O preço total das frutas é:", preco_total)    
