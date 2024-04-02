class AirlinesTicketsManager:
    _bought_tickets = ["passagem_falsa"]

    def add_tickets(self, tickets):
        self._bought_tickets.append(tickets)

    def show_tickets_list(self):
        return self._bought_tickets


class AirlinesTickets:
    def __init__(self, origin, destiny, price):
        self.origin = origin
        self.destiny = destiny
        self.price = price

    def __repr__(self):
        return f'{self.origin} {self.destiny} {self.price}'

