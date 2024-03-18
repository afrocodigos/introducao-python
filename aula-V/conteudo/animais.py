class Animal:
    nome = "Nome do meu animal"

    def __init__(self, patas):
        self.numero_patas = patas

    def som(self):
        return "UARGH!"


class Mamifero:
    nome = "nome do meu mamifero"


class Gato(Animal, Mamifero):
    nome = "Garfield"

    def som(self):
        return "Miau"


class Cachorro(Animal):
    nome = "Paçoca"

    def __init__(self, nome, patas):
        super().__init__(patas=patas)
        self.nome = nome

    def som(self):
        return "Au au"
