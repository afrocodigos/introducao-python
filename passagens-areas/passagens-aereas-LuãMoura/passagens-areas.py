class PassagemAerea:
    def __init__(self, origem, destino, preco):
        self.origem = origem
        self.destino = destino
        self.preco = preco

    def __str__(self):
        return f"Origem: {self.origem}, Destino: {self.destino}, Preço: R${self.preco:.2f}"
    
# PassagemAerea é a classe que representa uma passagem aérea, com tributos de origem, destino e preço.

class PassagensAereasManager:
    def __init__(self):
        self.passagens = []

    def adicionar_passagem(self, passagem):
        self.passagens.append(passagem)

    def listar_passagens(self):
        for i, passagem in enumerate(self.passagens, start=1):
            print(f"Passagem {i}: {passagem}")

    def menu(self):
        while True:
            print("\n===== Menu de Opções =====")
            print("1. Comprar Passagem")
            print("2. Listar Passagens Compradas")
            print("3. Sair do Programa")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                origem = input("Digite a origem: ")
                destino = input("Digite o destino: ")
                preco = float(input("Digite o preço da passagem: R$"))
                nova_passagem = PassagemAerea(origem, destino, preco)
                self.adicionar_passagem(nova_passagem)
                print("Passagem comprada com sucesso!")

            elif opcao == "2":
                print("\nPassagens Compradas:")
                self.listar_passagens()

            elif opcao == "3":
                print("Encerrando o programa...")
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

# PassagensAereasManager é a classe que gerencia as passagens, com métodos para adicionar passagens e listar passagens compradas.
                
# Função principal para executar o programa
def main():
    gerenciador_passagens = PassagensAereasManager()
    gerenciador_passagens.menu()


if __name__ == "__main__":
    main()