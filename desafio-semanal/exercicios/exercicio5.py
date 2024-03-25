# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

preco_original = float(input("Digite o preço original do produto: "))
desconto_percentual = float(input("Digite o desconto percentual (em %): "))

desconto_valor = preco_original * desconto_percentual / 100
preco_final = preco_original - desconto_valor

print("Preço final do produto:", preco_final)