# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.

#Resposta


preco = float(input("Digite o preço do produto: R$")) 
porcentagem = int(input("Qual foi a porcentagem do desconto? ")) 
novo_preco = preco - (preco * porcentagem / 100)
print(f"O preço final do produto após aplicar um desconto de {porcentagem}% é de: R${novo_preco:.2f}")