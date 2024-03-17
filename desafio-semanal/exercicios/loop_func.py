def loop_input():
    print("Insira cada valor da lista e pressione enter. Quando terminar de inserir itens na lista, digite 'Sair'")

    lista_usuario = []
    item_entrada = input("Insira a sua entrada: ")

    while item_entrada != "Sair":
        lista_usuario.append(item_entrada)
        item_entrada = input("Insira a sua entrada: ")
    
    return lista_usuario
