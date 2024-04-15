class PassagemAerea:
    def __init__(self, origem, destino, preco): #Construtor
        self.origem = origem
        self.destino = destino
        self.preco = preco
    
    def __str__(self):
        return f'Origem: {self.origem}, Destino: {self.destino}, Preço: R${self.preco:.2f}'
