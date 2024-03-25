# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

def calcular_preco_total():
    preco_total = 0  # inicializa a variável para armazenar o preço total
    frutas = {}  # dicionario(chave:valor) para armazenar o nome e o preço de cada fruta
    
    while True:
        nome = input("Digite o nome da fruta")
        if nome == '0':
            break  # Sai do loop se o usuário digitar 0
        
        try:
            preco = float(input("Digite o preço da fruta: "))
            if preco < 0:
                print("Digite um preço válido.")
                continue
        except ValueError:
            print("Digite um preço válido.")
            continue
        
        frutas[nome] = preco  # Adiciona a fruta e seu preço ao dicionário
        preco_total += preco  # Adiciona o preço ao preço total
    
    return frutas, preco_total

# Chama a função para calcular o preço total e obter o dicionário de frutas
frutas, total = calcular_preco_total()

# Imprime o nome das frutas e o preço total
print("\nLista dos produtos")
for fruta, preco in frutas.items():
    print(f"{fruta}: R${preco:.2f}")
print(f"\nPreço total: R${total:.2f}")
