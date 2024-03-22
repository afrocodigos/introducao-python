# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

# Implementação:
frutas = ["Maçã", "Uva", "Pera", "Manga", "Limão", "Abacaxi", "Cupuaçu"]
preco_soma = 0.0

for fruta in frutas:
    preco_soma += float(input(f'Insira o preço para a(o) {fruta}: '))

print(f'O preço final foi de R${preco_soma:.2f}')