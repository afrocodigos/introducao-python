# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.

totalPrice = 0  
   
while True:
        
        price = input("Insira o preço da fruta (ou digite 'total' para encerrar): ")

        if price == 'total':
            break

        totalPrice += float(price)

    
print(f"O preço total das frutas é: R${totalPrice:.2f}")