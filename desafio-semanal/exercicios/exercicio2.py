# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

# respondido por Lucas Teles.

def calc_preco():
    precos = []
    qnt_frutas = 8

    print("Você pode adicionar até 8 frutas ou digitar 'fim' para encerrar!")
    while len(precos) < qnt_frutas: 
        preco = input("Digite o valor da fruta: ")
        
        if preco.lower() == 'fim':
              break
        else:
            precos.append(float(preco))
            
    
    preco_total = sum(precos)
    return preco_total

preco_total = calc_preco()
print("O preço total das frutas é:", preco_total)