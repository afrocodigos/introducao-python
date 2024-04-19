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
    print("Você escolheu 'Comprar Passagens': ")
    origem = input("Qual é o seu local de origem? ")
    destino = input("Qual é o seu local de destino? ")
    preço = float(input("Qual o preço da passagem? "))
    
    return origem, destino, preço

def lista_passagens(passagens_adquiridas):
    for indice, passagem in enumerate(passagens_adquiridas):
        print(f"{indice+1}) {passagem}")