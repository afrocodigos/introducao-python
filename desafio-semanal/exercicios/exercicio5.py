# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

# respondido por Lucas Teles.

def calc_preco_final(preco_total, desconto):
    preco_desc = preco_total * (1 - desconto / 100)
    return preco_desc
print("Calcule o desconto do seu produto!")

preco_total = float(input("Digite o valor total do produto: "))
desconto = float(input("Digite o percentual de desconto(%): "))

preco_desc = calc_preco_final(preco_total, desconto)
preco_final = '{:.2f}'.format(preco_desc)

print("O preço final do seu produto com desconto é:", preco_final)