class PassagensAereasManager():

    def adicionar_passagem(self, passagem):
        self.passagens_compradas.append(passagem)

    def listar_passagens(self):
        return self.passagens_compradas

class Passagem:  
    def __init__(self, origem, destino, preco):
        self.origem = origem
        self.destino = destino
        self.preco = preco

    def __repr__(self):
        return f"{self.origem}, {self.destino}, {self.preco}"