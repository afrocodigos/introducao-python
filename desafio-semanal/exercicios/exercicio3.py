# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.

class Fruteira():
  frutas_adicionadas = []

  def adicionar_fruta(self, fruta):
    self.frutas_adicionadas.append(fruta)

while True:
  fruteira = Fruteira()

  fruta = input("Infome o nome de uma fruta: ")
  
  fruteira.adicionar_fruta(fruta)

  frutas_ordenadas = fruteira.frutas_adicionadas
  frutas_ordenadas.sort(key=str.lower)

  print() 
  print("*" * 100)
  print("LISTA DE FRUTAS")

  for indice, fruta in enumerate(frutas_ordenadas):
    print(f"{indice+1}) {fruta}")

  print("*" * 100)
  print()