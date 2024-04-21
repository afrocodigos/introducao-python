# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

contador = 0

class GeradorDescontos():

    def aplicar_desconto(self, percentual_desconto, preco_produto):
        valor_percentual = percentual_desconto / 100
        valor_desconto =  valor_percentual * preco_produto
        
        return valor_desconto


while True:
    
    if contador == 0:
        contador = contador + 1
        produto = input("Informe o nome do produto: ")
    
    else: 
        print()
        print(
            "Escolha uma da opções abaixo: \n"
            "Digite 1 para continuar aplicando descontos \n"
            "Digite 2 para sair do programa \n"
        )
        print()
        
        entrada_do_usuario = int(input())

        if entrada_do_usuario == 2:
            print("Encerrando o programa, volte sempre!")
            break
        else: 
            produto = input("Informe o nome do produto: ")
    
    preco_produto = float(input("Informe o valor do produto: "))
    percentual_desconto = int(input("Informe percentual de desconto fornecido: "))
    
    gerador_desconto = GeradorDescontos()
    
    valor_desconto = gerador_desconto.aplicar_desconto(percentual_desconto, preco_produto)
    
    preco_final = locale.currency(preco_produto - valor_desconto, grouping=True)
    preco_produto_reais = locale.currency(preco_produto, grouping=True)

    print()
    print(f"O valor do(a) {produto} é de {preco_produto_reais}, mas com o desconto de {percentual_desconto}%, o valor final ficará {preco_final}.")
    print()