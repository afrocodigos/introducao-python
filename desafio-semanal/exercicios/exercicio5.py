# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.


value_prod = float(input("Digite o valor do produto= "))
percentage = float(input("Digite o valor do desconto= "))


if percentage > value_prod:
    print("O desconto não pode ser maior que o valor do produto.")
else:
    value_discount = value_prod * (percentage / 100)
    value_final = value_prod - value_discount    
    print("O preço final do produto após o desconto é:", value_final)