from Passagens import PassagensAreasManager,Passagem
from apresentacoes import mostra_menu,menu_cadastro,cancelar_passagem

while True:
    passagem_manager = PassagensAreasManager()#
    mostra_menu()
    entrada_usuario = int(input())
    if entrada_usuario == 1:
        origem,destino,preco = menu_cadastro()
        passagem = Passagem(origem,destino,preco)
        passagem_manager.adicionar_passagem(passagem)
    elif entrada_usuario == 2:
        print("Listar Passagem")
        for indice, passagem in enumerate(passagem_manager.lista_passagens_compradas):
            print(f"{indice+1}) - {passagem}")
    elif entrada_usuario == 3:
        cancelar_passagem(passagem_manager)
    elif entrada_usuario == 4:
        print("Você saiu do Programa!!!")
        break
