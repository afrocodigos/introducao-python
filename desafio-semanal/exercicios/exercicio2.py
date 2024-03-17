# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

def total_purchase():
    verify = True
    price_total = 0 
    description_items = f"{"-"*25}\n Descritivo da compra\n{"-"*25}\n"
    i = 0

    while(verify):
        i += 1

        fruit = float(input("Qual o valor da fruta: "))

        amount = float(input("Qual a quantidade dessa fruta: "))
        
        description_items += f"item {i} - preço: R$ {fruit:.2f} - quantidade {amount} - valor R$ {(fruit *  amount):.2f}\n"

        price_total += fruit * amount
        
        finish_loop = input("Deseja adicionar mais alguma fruta? [S/N]")

        while(True):
            if(finish_loop == "S" or finish_loop == "s"):
                break;
            elif (finish_loop == "N" or finish_loop == "n"):
                verify = False
                break;
            finish_loop = input("Digite uma opção válida. Deseja adicionar mais alguma fruta? [S/N]")

    return description_items + f"O preço total é de R$ {price_total:.2f}."

print(total_purchase())