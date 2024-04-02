def show_menu():
    print('-'*60)
    print('PASSAGENS AÉREAS \n\n'
        'Digite 1 para comprar passagens \n'
        'Digite 2 para listar passagens \n'
        'Digite 3 para sair do programa \n')
    print('-'*60)


def menu_buy_ticket():
    print('Você escolheu a opção comprar passagens')
    origin = input('Origem: ')
    destiny = input('Destino: ')
    price = float(input('Preço: '))
    return origin, destiny, price


def tickets_list(bought_tickets):
    for i, ticket in enumerate(bought_tickets):
        print(f'{i+1} - {ticket}')
