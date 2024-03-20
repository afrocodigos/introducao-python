class PassagensAreasManager():
    lista_passagens_compradas = []
    
    def adicionar_passagem(self,passagem):
        self.lista_passagens_compradas.append(passagem)
        
class Passagem:
    def __init__(self,origem,destino,preco):
        self.origem = origem
        self.destino = destino
        self.preco = preco
        
    def __repr__(self):
        return f"Origem: {self.origem} - Destino: {self.destino} - Preço: {self.preco}"