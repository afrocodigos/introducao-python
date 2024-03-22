# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

class Fruteira():
  frutas_adicionadas = []
  
  def adicionar_fruta(self, fruta):
    self.frutas_adicionadas.append(fruta)
  
  def listar_frutas(self):
    return self.frutas_adicionadas

class Fruta:
    def __init__(self, nome, preco):
      self.nome= nome
      self.preco = preco

    def __repr__(self):
      return  f"{self.nome} {self.preco}"
    
while True:
    fruteira = Fruteira()
    preco_total = 0

    nome = input("Infome o nome de uma fruta: ")
    preco = float(input(f"Infome o valor da(o) {nome}: "))

    fruta = Fruta(nome, preco)

    fruteira.adicionar_fruta(fruta)
    print() 
    print("*" * 100)

    for indice, fruta in enumerate(fruteira.frutas_adicionadas):
        preco_total += fruta.preco
        print(f"{indice+1}) Fruta: {fruta.nome} Preço: {fruta.preco}")

    print(f"PREÇO TOTAL DAS FRUTAS: R$ {preco_total}")  
    print("*" * 100)
    print()

              