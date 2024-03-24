# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

def recebe_frutas():
    print("Insira a quantidade de frutas:")
    qtd = int(input())

    print("Agora insira as frutas:")
    frutas = []
    for i in range(0, qtd):
        frutas.append(input())
    return frutas

def soma_frutas(frutas):
    sum = 0
    for i in range(0, len(frutas)):
        if frutas[i] == "pera":
            sum += 3
        elif frutas[i] == "maca":
            sum += 2
        elif frutas[i] == "melancia":
            sum += 8
    return sum


print(f"O valor da sua compra e: R${soma_frutas(recebe_frutas())}")


