# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não:
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.


def apply_discount(price, discount):
    discount_percent =  1 - discount / 100
    return f'O produto com valor R$ {price:.2f} aplicando desconto de {discount}% tem o valor final de R$ {(price * discount_percent):.2f}'

product_price = 200
product_discount = 15
print(apply_discount(product_price, product_discount))
