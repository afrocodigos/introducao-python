# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

price = float(input("Qual o valor do produto: "))
discount = float(input("Qual o valor do desconto (não precisa do símbolo de %): "))

def discount_price(price, discount):
    value = price * (1 - discount/100)
    return f"O valor de R${price:.2f} com o desconto de {discount}% fica R$ {value:.2f}"

print(discount_price(price, discount))