# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.
lista_numero = []
tamanho_do_vetor = int(input("Você que quantas frutas você quer: "))

for umaChave in range(tamanho_do_vetor):
    numero = int(input("Preço da fruta:"))
    lista_numero.append(numero)
soma = sum(lista_numero)
print(lista_numero)
print(f"Valor total pago em frutas: {soma}R$")