# Escreva um programa que remova todas as duplicatas de uma lista e imprima a lista resultante.

# Dicas que podem ser seguidas ou não: 
# Remover duplicatas de uma lista:
# - Você pode utilizar conjuntos (sets) para remover duplicatas, já que conjuntos não permitem elementos duplicados.
# - Caso queira, converta a lista para um conjunto. Em seguida, converta o conjunto de volta para uma lista.
# - Imprima a lista resultante.

class CriarLista():
  lista = []
  
  def adicionar_valor(self, valor):
    self.lista.append(valor)

while True:
    print("==" * 50)
    print("Escolha uma das opções abaixo:")
    print("Digite 1 para inserir um valor na lista")
    print("Digite 2 para sair do programa")
    print("==" * 50)
    print()
    
    entrada_do_usuario = int(input())
    
    if entrada_do_usuario == 1:
      valor = input("Infome o valor: ")

      CriarLista().adicionar_valor(valor)
        
      conjunto = set(CriarLista().lista)
      tamanho_lista = len(CriarLista().lista)
      nova_lista = list(conjunto)
      tamanho_nova_lista = len(nova_lista)

      print()
      print("*" * 100)
      print(f"Lista: {CriarLista().lista}")
      print(f"Lista sem valores repetidos: {nova_lista}")
      print()
      print(f"A lista COMPLETA possui {tamanho_lista} elemento(s).")
      print(f"A lista SEM dados repetidos possui {tamanho_nova_lista} elemento(s).")
      print("*" * 100)
      print()
        
    elif entrada_do_usuario == 2:
      print("Encerrando o programa, volte sempre! ")
      break
    
    else:
        print("Opção inválida, por favor, digite uma opção correta!")
        print()