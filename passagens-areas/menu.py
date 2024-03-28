def show_menu():
    print("-" * 80)
    print("Escolha uma da opções abaixo:")
    print("Digite 1 para comprar passagens")
    print("Digite 2 para listar passagens")
    print("Digite 3 para sair do programa")
    print("-" * 80)
    print()

    
def menu_comprar_passagens():
    print("Você escolheu compra de passagens")
    origem = input("Qual é a origem?")
    destino = input("Qual é o destino?")
    preco = float(input("Qual é o preço?"))
    return origem,destino,preco
