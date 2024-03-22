# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

valor_produto = float(input("Informe o valor do produto ->"))
desconto_usuario = float(input("Informe o valor do desconto ->"))

desconto_em_real = valor_produto * desconto_usuario / 100
preco_final = valor_produto - desconto_em_real

print("##" *30)
print(f"Com um desconto de {desconto_usuario}% o valor final do produto é de {preco_final}")
print("##" *30)

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.