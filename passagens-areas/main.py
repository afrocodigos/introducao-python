from tickets import AirlinesTicketsManager, AirlinesTickets
from presentation import show_menu, menu_buy_ticket, tickets_list


while True:
    airlines_tickets_manager = AirlinesTicketsManager()

    show_menu()

    user_entry = int(input('Escolha uma das opções acima: '))


    if user_entry == 1:
        origin, destiny, price = menu_buy_ticket()

        ticket = AirlinesTickets(origin, destiny, price)
        airlines_tickets_manager.add_tickets(ticket)

    elif user_entry == 2:
        print('Você escolheu a opção listar passagens')

        tickets_list(airlines_tickets_manager.show_tickets_list())

    elif user_entry == 3:
        print('Você escolheu a sair, volte sempre!')
        print('-'*60)
        break

    else:
        print('Entrada inválida, tente novamente!')
