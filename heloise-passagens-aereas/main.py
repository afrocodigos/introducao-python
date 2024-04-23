from apresentacao import lista_passagens, menu, menu_comprar_passagem
from passagens import Passagem, PassagensAereasManager

while True :
    passagens_aereas_manager = PassagensAereasManager()

    menu()
  
    opcao = int (input())

    if opcao == 1 : 
       origem,destino,preco = menu_comprar_passagem()
       passagem = Passagem (origem,preco,destino)
       passagens_aereas_manager.adicionar_passagem(passagem)

    elif opcao == 2 :
       lista_passagens(passagens_aereas_manager.listar_passagens())

    else :
      print("Volte Sempre! ")
      break