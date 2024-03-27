# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

def Menu():
    while True:
        preco = float(input("Qual o preço do seu produto?"))
        desconto = float(input("Qual a percentagem de desconto? (em %)"))

        valor_desconto = (desconto / 100) * preco
        preco_final = preco - valor_desconto

        print(f"O preço do produto com desconto é: R${preco_final:.2f}")

        # Inserindo lógica simples para que o usuário possa fazer um novo cálculo.
        continuar = input("Deseja calcular o desconto de outro produto? (s/n) ")
        if continuar.lower() != 's':
            break

Menu()