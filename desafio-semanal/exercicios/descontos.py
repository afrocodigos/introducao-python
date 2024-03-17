class OperacoesProdutos:
    def valortotal(self,numero_1,numero_2):
        return numero_1 * numero_2

    def descontoproduto(self,numero_1,numero_2):
        return numero_1 * (numero_2/100)
    
    def valorfinal(self,numero_1,numero_2):
        return numero_1 - numero_2