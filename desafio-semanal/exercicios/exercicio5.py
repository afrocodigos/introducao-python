# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

def calcular_preco_final(preco_original, desconto_percentual):
    desconto = (desconto_percentual / 100) * preco_original
    preco_final = preco_original - desconto
    return preco_final

# Solicita ao usuário o preço original do produto e o desconto percentual
preco_original = float(input("Digite o preço original do produto: "))
desconto_percentual = float(input("Digite o desconto percentual (%): "))

# Calcula o preço final
preco_final = calcular_preco_final(preco_original, desconto_percentual)

# Imprime o preço final
print(f"O preço do produto com o desconto de {desconto_percentual} % é: R${preco_final:.2f}")
