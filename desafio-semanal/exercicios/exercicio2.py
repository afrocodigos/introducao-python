# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Primeiramente, defini uma lista chamada frutas, onde contem as frutas que irei atribuir o valor
frutas= [ "acelora", "manga", "jabuticaba", "melão", "uva"]

#Criei uma variavel para armazernar o preço total das frutas.
preco_total = 0

#Portanto, foi necessário cria um loop para entradas dos preços de cada fruta.
for fruit in frutas:
    preco = float(input(f"Insira o preço da {fruit}: "))
    preco_total += preco


print()
print(f"O preço total das frutas é: R$ {preco_total:.2f}")
print()