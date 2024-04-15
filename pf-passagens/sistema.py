## Importando as classes
from PassagemAerea import PassagemAerea as Passagem
from Manager import Manager 

def gerar_passagens():
    passagens = []
    passagens.append(Passagem('Rio de Janeiro', 'São Paulo', 200.0))
    passagens.append(Passagem('Rio de Janeiro', 'Belo Horizonte', 300.0))
    passagens.append(Passagem('Rio de Janeiro', 'Curitiba', 400.0))
    passagens.append(Passagem('Rio de Janeiro', 'Salvador', 500.0))
    passagens.append(Passagem('Rio de Janeiro', 'Recife', 600.0))
    passagens.append(Passagem('Rio de Janeiro', 'Fortaleza', 700.0))
    return passagens

def menu():
    manager = Manager([])
    passagens = gerar_passagens()
    for passagem in passagens:
        manager.adicionar_passagem(passagem)
    compradas = []
    while True:
        print("1 - Listar passagens")
        print("2 - Comprar passagens")
        print("3 - Listar passagens compradas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            manager.listar_passagens()
        elif opcao == '2':
            opt = manager.listar_passagens()
            print("Realize a compra da passagem")
            compra = int(input("Digite o número da passagem que deseja comprar: "))
            origem = passagens[compra-1].origem
            destino = passagens[compra-1].destino
            preco = passagens[compra-1].preco
            passagem = Passagem(origem, destino, preco)
            manager.adicionar_passagem(passagem)
            compradas.append(passagem)
        elif opcao == '3':
            for passagem in compradas:
                print(passagem)
        elif opcao == '4':
            break
        else:
            print("Opção inválida")

menu()