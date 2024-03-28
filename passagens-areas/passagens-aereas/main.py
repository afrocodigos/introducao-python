from opcoes import mostrar_menu, comprar_passagem, listar_passagem

while True:
    mostrar_menu()

    entrada_usuario = input()

    if entrada_usuario == "1":
        print("Você escolheu comprar uma passagem")
        comprar_passagem()

    elif entrada_usuario == "2":
        print("Você escolheu listar passagens")
        listar_passagem()

    elif entrada_usuario == "3":
        print("Você saiu do programa")
        break
    else:
        print("Entrada inválida. Por favor, insira uma das opções listadas.")
