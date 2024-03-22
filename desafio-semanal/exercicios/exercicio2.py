# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

qtd_frutas = int(input("Informe quantas frutas deseja inserir ->"))
preco_total_frutas = 0.0

for i in range(qtd_frutas):
    preco_total_frutas += float(input(f"Insira o valor da fruta {i+1} -> "))
    
print("##" *20)
print(f"O valor total das frutas é de {preco_total_frutas} reais")
print("##" *20)

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.