def mostra_menu():
    print("==" * 50)
    print(
        "Escolha uma da opções abaixo: \n"
        "Digite 1 para comprar passagens \n"
        "Digite 2 para listar passagens \n"
        "Digite 3 para sair do programa \n"
    )
    print("==" * 50)
    print()


def menu_compra_passagem():
    print("Você escolheu comprar de passagens")
    origem = input("Qual é a origem? ")
    destino = input("Qual é a destino? ")
    preço = float(input("Qual é a preço? "))
    
    return origem, destino, preço

def lista_passagens(passagens_compradas):
    for indice, passagem in enumerate(passagens_compradas):
        print(f"{indice+1}) {passagem}")