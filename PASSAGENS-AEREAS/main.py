from passagens import PassagensAereasManager, Passagem
from apresentacao import mostrar_menu, menu_compra_passagem, lista_passagens

while True:
    passagens_aereas_manager = PassagensAereasManager()
    mostrar_menu()

    # Recceber a entrada do usuário
    entrada_do_usuario = int(input()) #Se inserir uma letra terá erro

    if entrada_do_usuario == 1:
        passagem = Passagem(*menu_compra_passagem())
        passagens_aereas_manager.adicionar_passagem(passagem)
    
    elif entrada_do_usuario == 2:
        lista_passagens(passagens_aereas_manager.listar_passagens())
    # se o usuário escolher sair do programa, usar break para encerrar o programa
    elif entrada_do_usuario == 3:
        break
