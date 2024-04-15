class Manager:
    passagens = []

    def __init__(self, passagens):
        self.passagens = passagens
    
    def listar_passagens(self):
        if len(self.passagens) == 0:
            print("Nenhuma passagem cadastrada")
            return
        i = 1
        for passagem in self.passagens:
            print(f'{i} - {passagem}')
            i += 1
        return self.passagens
    
    def adicionar_passagem(self, passagem):
        self.passagens.append(passagem)

