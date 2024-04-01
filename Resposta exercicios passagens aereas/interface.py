# interface.py
from gerenciador import PassagensAereasManager
from passagem import PassagemAerea  # Adicionando essa linha de importação

def comprar_passagem(manager):
    origem = input("Origem: ")
    destino = input("Destino: ")
    preco = float(input("Preço: "))
    passagem = PassagemAerea(origem, destino, preco)
    manager.adicionar_passagem(passagem)
    print("Passagem comprada com sucesso!")

def menu():
    print("\n=== AfroCodigosFy - Venda de Passagens no Precinho ===")
    print("1. Comprar Passagem")
    print("2. Listar Passagens Compradas")
    print("3. Sair")

def executar():
    manager = PassagensAereasManager()
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            comprar_passagem(manager)
        elif opcao == "2":
            manager.listar_passagens()
        elif opcao == "3":
            print("Obrigado por utilizar o AfroCodigosFy. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    executar()

