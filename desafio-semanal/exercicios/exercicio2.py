# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não:
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.


def init(item):
    print('-'*65)
    print(f'Calculadora de preços de {item}.')
    print('Digite valores a serem somados ou 0 para receber valor o total:')
    print('-'*65)
    user_entry()


def user_entry():
    user_entry_values = []

    while True:
        user_entry = input('Valor: R$ ')
        user_entry = float(user_entry.replace(',', '.'))
        user_entry_values.append(user_entry)

        if(user_entry == 0):
            print(show_result(user_entry_values))
            break


def show_result(user_entry_values):
    print('-'*65)
    return f'O valor total é R$ {sum(user_entry_values):.2f}'


items_type = 'frutas'
init(items_type)
