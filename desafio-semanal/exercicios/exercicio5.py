# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

def calcular_preco_final(preco_produto, desconto): 
    preco_final = preco_produto - (preco_produto * (desconto/100))
    return preco_final

preco_produto = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o valor do desconto percentual (%): "))

preco_final = calcular_preco_final(preco_produto,desconto)

print(f"O preço do produto após o desconto de {desconto}% é: {preco_final: .2f}R$")

