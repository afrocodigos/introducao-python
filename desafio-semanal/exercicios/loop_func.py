def loop_input()):
    print("Insira cada valor da lista e pressione enter. Quando terminar de inserir itens na lista, digite 'Sair'")

    lista_entrada_usuario = []
    item_entrada = input("Insira a sua entrada: ")

    while item_entrada != "Sair":
        lista_entrada_usuario.append(item_entrada)
        item_entrada = input("Insira a sua entrada: ")
