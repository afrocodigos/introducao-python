# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

preco_original = float(input("Digite o preço oiginal do produto: "))
desconto_percentual = float(input("Digite o desconto percentual: "))

def calcular_desconto(preco, desconto):
    return preco - (preco * desconto) / 100

resultado = format(calcular_desconto(preco_original, desconto_percentual), '.2f')
print(f"O preço final é de: R${resultado}")