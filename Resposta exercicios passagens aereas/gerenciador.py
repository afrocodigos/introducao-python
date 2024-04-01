# gerenciador.py
from passagem import PassagemAerea

class PassagensAereasManager:
    def __init__(self):
        self.passagens = []

    def adicionar_passagem(self, passagem):
        self.passagens.append(passagem)

    def listar_passagens(self):
        if not self.passagens:
            print("Nenhuma passagem foi comprada ainda.")
        else:
            print("Passagens compradas:")
            for idx, passagem in enumerate(self.passagens, start=1):
                print(f"{idx}. Origem: {passagem.origem}, Destino: {passagem.destino}, Preço: {passagem.preco}")

