# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

frutas = []
preco_total = 0

def sair(opcao):
    return opcao.lower().strip() == 'sair'

def nome_fruta():
    while True:
        fruta = input("Digite o nome da fruta ou 'sair' para encerrar: ").strip().lower()
        if sair(fruta):
            return None
        elif fruta:
            return fruta
        else:
            print("Nome de fruta inválido. Tente novamente.")

def preco_fruta():
    while True:
        preco_str = input("Digite o preço da fruta: ").strip().replace(",", ".")
        if sair(preco_str):
            return None
        try:
            preco = float(preco_str)
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
            else:
                return preco
        except ValueError:
            print("Preço inválido. Tente novamente.")

def adicionar_fruta(fruta, preco):
    global preco_total
    frutas.append((fruta, preco))
    preco_total += preco
    print(f"O preço da fruta {fruta.capitalize()} é R$ {preco:.2f}.")

while True:
    nome = nome_fruta()
    if nome is None:
        break
    preco = preco_fruta()
    if preco is None:
        break
    adicionar_fruta(nome, preco)
    print(f"\nPreço total das frutas: R$ {preco_total:.2f}\n")
    continuar = input("Deseja adicionar outra fruta? (s/n): ").strip().lower()
    if continuar != 's':
        break

print(f"\nPreço total de todas as frutas: R$ {preco_total:.2f}")
