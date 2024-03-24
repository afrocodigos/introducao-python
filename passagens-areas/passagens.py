class PassagensAereasManager:
    _passagens_compradas = []

    def adicionar_passagem(self, passagem):
        self._passagens_compradas.append(passagem)

    def listar_passagens(self):
        return self._passagens_compradas


class Passagem:
    def __init__(self, origem, destino, preço):
        self.origem = origem
        self.destino = destino
        self.preço = preço

    def __repr__(self):
        return f"{self.origem} {self.destino} {self.preço}"
