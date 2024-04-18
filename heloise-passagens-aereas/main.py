from apresentacao import menu
from passagens import Passagem, PassagensAereasManager


while True :
    passagens_aereas_manager = PassagensAereasManager()

    menu()
  
    opcao = int (input())

    if opcao == 1 : 
       print("Comprar passagens ")
       origem = input("Qual a origem?")
       destino = input("Qual o destino ?")
       preco = float(input("Qual o preço?"))

       passagem = Passagem(origem, destino,  preco)

       passagens_aereas_manager.adicionar_passagem(passagem)

    elif opcao == 2 :
       print (" Listar passagens")
       print(passagens_aereas_manager.passagens_compradas)

    else :
      print("Volte Sempre! ")
      break