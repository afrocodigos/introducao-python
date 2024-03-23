# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.


def calcular_preco_final(preco_original, desconto_percentual):

  valor_desconto = preco_original * (desconto_percentual / 100)
  preco_final = preco_original - valor_desconto
  return preco_final

preco_original = float(input("Digite o preço original do produto: R$ "))


desconto_percentual = float(input("Digite o desconto percentual (sem o símbolo %): "))


preco_final = calcular_preco_final(preco_original, desconto_percentual)


print(f"Preço original: R${preco_original:.2f}")
print(f"Desconto: {desconto_percentual:.2f}%")
print(f"Preço final: R${preco_final:.2f}")