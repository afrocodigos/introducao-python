from classPassagem import PassagemAerea, PassagemAereaManager
controle_passagens = PassagemAereaManager()

def mostrar_menu():
    print("="*100)
    print("Digite 1 para comprar uma passagem aérea")
    print("Digite 2 para listar passagens aéreas")
    print("Digite 3 para sair")
    print("="*100)

def listar_passagem():
    print("Passagens atuais:")
    controle_passagens.lista_passagem()

def comprar_passagem():
    origem_viagem = input("Digite qual a origem da sua viagem: ")
    destino_viagem = input("Digite qual o destino da sua viagem: ")
    preco_viagem = float(input("Digite qual o valor da sua viagem: "))

    passagem_atual = PassagemAerea(origem=origem_viagem, destino=destino_viagem, preco=preco_viagem)
    controle_passagens.compra_passagem(passagem_atual.cod_passagem)
    print()
    print(f"Sua passagem: {passagem_atual.cod_passagem}")
