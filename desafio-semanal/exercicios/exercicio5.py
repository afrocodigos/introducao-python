# AfroCódigos 2024
# Autora: Alfa Marine

# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Cria função que calcula preço após desconto
def calcula_preco_desconto(preco_original=0, desconto_percentual=1.0):
    preco_desconto = preco_original*((100-desconto_percentual)/100)
    return round(preco_desconto,2)

# Testa a função de desconto
precos_total_original = float(input("Insira o preço original: R$ "))
desconto = int(input("Insira o valor de desconto(%): "))
preco_total_desconto = calcula_preco_desconto(precos_total_original,desconto)

print()
print(f"Preço total após o desconto de {desconto}%: R$ {preco_total_desconto}")
