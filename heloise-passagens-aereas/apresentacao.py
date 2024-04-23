def menu() :
     print("=="*25)
     print(
        "Escolha uma das opções abaixo:\n" 
        "1-para comprar passagens\n"
        "2-para listar passagens\n"
        "3-pra sair do programa "
        )
     print("=="*25)
     print()

def menu_comprar_passagem() :
      print("Comprar passagens ")
      origem = input("Qual a origem?")
      destino = input("Qual o destino ?")
      preco = float(input("Qual o preço?"))

      return origem, destino, preco 

def lista_passagens(passagens_compradas):
    for indice, passagem in enumerate(passagens_compradas) :
         print(f"{indice+1}) {passagem}")
