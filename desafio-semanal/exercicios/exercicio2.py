# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

preco_frutas = []

while True:

    # Utilizando uma variável de estado para que o programa saiba qual operação realizar.
    # Esse comportamento permite que o usuário adicione mais frutas após o cálculo da soma.
    estado = int(input("---------------HOME---------------\n"
                       "1. Adicionar preço em suas frutas\n"
                       "2. Somar preço das frutas\n"
                       "3. Sair\n"))

    if estado == 1:
        preco = int(input("Insira o preço das frutas: "))
        preco_frutas.append(preco) # Inserção do preço da fruta na lista que demonstra o carrinho do usuário
        print(preco_frutas)

    if estado == 2:
        resultado = sum(preco_frutas) # Soma de todos os valores inseridos.
        print("O valor total das frutas é de R$", resultado)

    if estado == 3:
        break

# Pesquisa de novas formas de implementar o mesmo programa.
    
# Utilizando o paradigma do encapsulamento, estamos concentrando as lógicas em funções para tornar o códio mais fácil de entender.

# Permitindo o usuário adicionar não só o preço mas também o nome da fruta, nesse caso é necessário utilizarmos a estrutura dict.
    
def adicionar_preco(frutas):
    nome_fruta = input("Insira o nome da fruta: ")
    preco = float(input("Insira o preço da fruta: "))
    frutas[nome_fruta] = preco # Adicionando a fruta ao dicionário que foi aberto no Menu
    print(f"Preço de {nome_fruta}, {preco} adicionado com sucesso.")

def calcular_total(frutas):
    if not frutas:
        print("Não há frutas adicionadas.")
        return
    total = sum(frutas.values()) # Soma dos valores inseridos no dicionário
    print(f"O valor total das frutas ({', '.join(frutas.keys())}) é de R${total}")

def menu():
    frutas = {}
    while True:
        print("---------------HOME---------------")
        print("1. Adicionar preço em uma fruta")
        print("2. Somar preço das frutas")
        print("3. Sair")
        estado = int(input("Escolha uma opção: "))
        if estado == 1:
            adicionar_preco(frutas)
        elif estado == 2:
            calcular_total(frutas)
        elif estado == 3:
            break
        else:
            print("Opção inválida, tente novamente.")

menu() # Execução do programa.
