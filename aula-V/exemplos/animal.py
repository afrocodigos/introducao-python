class Animal():
    nome = "nome do animal"

    def __init__(self, patas):
        self.numero_patas = patas

    def som(self):
        return "UARGH"

class Mamifero():
    nome = "nome do mamífero"

class Gato(Animal, Mamifero):
    def som(self):
        return "Miau"
    
class Cachorro(Mamifero, Animal):
    def som(self):
        return "Au au"