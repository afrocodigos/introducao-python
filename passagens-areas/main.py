
from menu import show_menu, menu_comprar_passagens
from passagens import Passagem, PassagensAereasManager

# Começo do loop principal do programa
while True:
    # A cada iteração do loop, eu crio uma nova instância da classe PassagensAereasManager
    passagens_aereas_manager = PassagensAereasManager()
   
   # Nesta função, mostro o menu para o usuário
    show_menu()

    # Solicito ao usuário que escolha uma opção e guardo essa opção como um inteiro.
    entrada_do_usuario = int(input(f"Digite a sua opção :"))
    
    # Verifico qual opção o usuário escolheu
    if entrada_do_usuario == 1:
        origem, destino, preco = menu_comprar_passagens()
        passagem = Passagem(origem, destino, preco)
        passagens_aereas_manager.adicionar_passagem(passagem)

    elif entrada_do_usuario == 2:

        for passagem in passagens_aereas_manager.passagens_compradas:
            print(passagem)
       
    else:
        print("Opção inválida!!!\nPor favor, veja o menu e escolha uma opção válida.")
        
    # Se o usuário escolheu a opção 3, imprimo uma mensagem de encerramento e
    # saio do loop, encerrando o programa
    if entrada_do_usuario == 3:
        print()
        print("Encerrando o programa. Volte sempre!!!")
        print()
        break


