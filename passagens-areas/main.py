from passagens import Passagem, PassagensAereasManager
from apresentacao import menu_compra_passagem, mostra_menu, lista_passagens


while True:
    passagens_aereas_manager = PassagensAereasManager()

    mostra_menu()

    entrada_do_usuario = int(input())

    if entrada_do_usuario == 1:
        origem, destino, preço = menu_compra_passagem()
        passagem = Passagem(origem, destino, preço)
        passagens_aereas_manager.adicionar_passagem(passagem)
    elif entrada_do_usuario == 2:
        lista_passagens(passagens_aereas_manager.listar_passagens())
    elif entrada_do_usuario == 3:
        print("Encerrando o programa, volte sempre!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
