class PassagensAereas:
    _passagens_adquiridas = []

    def adc_passagem(self, passagem):
        self._passagens_adquiridas.append(passagem)

    def listar_passagens(self):
        return self. _passagens_adquiridas   
class Passagem:
    def __init__(self, origem, destino, preço):
        self.origem = origem
        self.destino = destino
        self.preço = preço

    def __repr__(self):
        return f"{self.origem} {self.destino} {self.preço}"