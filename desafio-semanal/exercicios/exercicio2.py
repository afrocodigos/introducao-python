# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.
prices = []
while True:
    price = input("Digite o preço das frutas (ou digite 'sair' para finalizar): ")
    if price == "sair":
        break
    try:
        prices.append(float(price))
    except ValueError:
        print("Valor inválido. Digite um número.")

valor_decimal = "{:.2f}".format(sum(prices))
print(f"Total frutas: R${valor_decimal}")