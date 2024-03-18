# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

preco_frutas = []

while True:

    estado = int(input("---------------HOME---------------\n"
                       "1. Adicionar preço em suas frutas\n"
                       "2. Somar preço das frutas\n"
                       "3. Sair\n"))

    if estado == 1:
        preco = int(input("Insira o preço das frutas: "))
        preco_frutas.append(preco)
        print(preco_frutas)

    if estado == 2:
        resultado = sum(preco_frutas)
        print("O valor total das frutas é de R$", resultado)

    if estado == 3:
        break

# ChatGPT me indicou implantar as seguintes melhorias
    
# Validação de entrada: Adicione alguma validação para garantir que o usuário insira um preço válido para as frutas. Por exemplo, verifique se o preço é um número positivo ou se é um número real.

# Melhoria da interface do usuário: Você pode adicionar mensagens mais amigáveis ou instruções claras para orientar o usuário. Além disso, pode ser útil incluir uma opção de voltar ao menu principal após a execução de uma operação.

# Usabilidade: Permita que o usuário insira o nome da fruta junto com o preço, para que ele saiba a que fruta o preço se refere. Isso pode ser feito utilizando um dicionário em vez de uma lista para armazenar os preços.

# Encapsulamento: Considere encapsular a lógica em funções para tornar o código mais modular e fácil de entender.
    
def adicionar_preco(frutas):
    nome_fruta = input("Insira o nome da fruta: ")
    preco = float(input("Insira o preço da fruta: "))
    frutas[nome_fruta] = preco
    print(f"Preço de {nome_fruta}, {preco} adicionado com sucesso.")

def calcular_total(frutas):
    if not frutas:
        print("Não há frutas adicionadas.")
        return
    total = sum(frutas.values())
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

menu()
