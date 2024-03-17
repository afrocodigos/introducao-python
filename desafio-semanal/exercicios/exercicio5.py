# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

preco_original = float(input("Qual é o preço original do produto? "))

desconto_percentual = float(input("Qual é o desconto percentual aplicado? "))

preco_final = preco_original - (preco_original * (desconto_percentual / 100))

print("O preço final do produto após o desconto é:", preco_final)
