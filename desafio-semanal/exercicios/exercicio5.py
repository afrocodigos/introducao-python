# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

#Implementação
resposta = input("Entre com o preço do produto e o desconto (xx.xx %xx)") #Entrando numa linha só
resposta = resposta.split(" ")
if len(resposta) != 2:
    raise ValueError("Tome cuidado com a entrada. Respeite o modelo.")
preco = float(resposta[0])
resposta[1] = resposta[1].replace("%","")
desconto = float(resposta[1])

preco_final = preco - (preco * (desconto/100))
print(f'Preço após aplicar o desconto: R${preco_final:.2f}')