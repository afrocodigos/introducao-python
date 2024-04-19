from passagens import Passagem, PassagensAereas
from apresentacao import menu_compra_passagem, mostra_menu, lista_passagens

while True:
    passagens_aereas = PassagensAereas()
    mostra_menu()
    entrada_do_usuario = int(input())

    if entrada_do_usuario == 1:
        origem, destino, preço = menu_compra_passagem()
        passagem = Passagem(origem, destino, preço)
        passagens_aereas.adc_passagem(passagem)

    elif entrada_do_usuario == 2:
        print("Você escolheu 'Listar Passagens': ")
        lista_passagens(passagens_aereas.listar_passagens())
    else:
        print("Encerrando a sessão, volte sempre!")
        break