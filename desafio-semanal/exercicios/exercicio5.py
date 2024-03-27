# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

def calcular_preco_final(preco, desconto):
    promocao = (1 - (desconto / 100))
    preco_final = preco * promocao
    print(f"O preço final do produto com {desconto}% de desconto é R$ {preco_final:.2f}.")

def obter_valor(mensagem):
    while True:
        valor_str = input(mensagem).strip().replace(",", ".")
        try:
            valor = float(valor_str)
            if valor < 0:
                print("O valor não pode ser negativo. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")

preco = obter_valor("Digite o preço do produto: ")
desconto = obter_valor("Digite o desconto percentual: ")

if preco is not None and desconto is not None:
    calcular_preco_final(preco, desconto)
else:
    print("Operação cancelada.")
