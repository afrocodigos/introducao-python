class PassagemAerea():
    def __init__(self, origem, destino, preco):
        self.cod_origem = origem
        self.cod_destino = destino
        self.valor_preco = preco
        self.cod_passagem = {"Origem": origem,
                             "Destino": destino,
                             "Preço": preco}

class PassagemAereaManager():
    _lista_passagens = []

    def compra_passagem(self,passagem):
        self._lista_passagens.append(passagem)

    def lista_passagem(self):
        for item_passagem in self._lista_passagens:
            print(item_passagem)

