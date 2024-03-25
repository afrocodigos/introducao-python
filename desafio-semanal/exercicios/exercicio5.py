# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

frutas = []
total = 0 

while True:
    fruta = input("Digite o nome da fruta (ou 'sair' para parar): ")
    if fruta == "sair":
        break
    preco = float(input("Digite o preço da fruta: "))
    frutas.append(fruta)
    total += preco

    print("Você comprou:", frutas)
    print("Preço total:" , total)