# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

print("Vamos fazer feira? ")
print()
print("=" * 20)

frutas = {}
total_valor = 0

def adicionar_fruta():
    global total_valor
    nome_fruta = input("Digite o nome da fruta: ")
    valor_fruta = input(f"Digite o valor da fruta {nome_fruta}: ")
    frutas[nome_fruta] = valor_fruta
    total_valor += int(valor_fruta)

def main():
    continuar = True
    while continuar:
        adicionar_fruta()
        resposta = input("Deseja adicionar outra fruta? (s/n): ")
        if resposta.lower() != 's':
            continuar = False

    print("\nLista de frutas e seus valores:")
    print()
    for fruta, valor in frutas.items():
        print(f"{fruta}: R${valor}")
    
    print(f"\nValor total das frutas: R${total_valor}")

if __name__ == "__main__":
    main()