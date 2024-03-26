def mostra_menu():
    print("--"*50)
    print(f"Escolha uma das opções Abaixo: \n Digite 1 para comprar passagens \n Digite 2 para listar passagens \n Digite 3 para deletar uma passagem \n Digite 4 para sair do programa")
    print("--"*50)

def menu_cadastro():
    print("Entrou na compra de passagens")
    origem = str(input("Qual e a origem: "))
    destino = str(input("Qual é o destino: "))
    preco = float(input("O preço da viagem: "))
    return origem,destino,preco

def cancelar_passagem(passagem_manager):
    deletar = str(input("Você que mesmo deletar a passagem: \n Responda com SIM ou NÃO \n"))
    if deletar.lower() == "sim":
        indice = int(input("Digite o indice da passagem que vc quer deletar: "))
        del passagem_manager.lista_passagens_compradas[indice - 1]
        print("Passagem cancelada")
    else:
        print("Você não concluiu o cancelamento da passagem")