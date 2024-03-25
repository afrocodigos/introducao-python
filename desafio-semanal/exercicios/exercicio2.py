# Crie um programa que permita ao usuário inserir o preço de várias frutas e, em seguida, calcule o preço total.

# Dicas que podem ser seguidas ou não: 
# - Crie um loop para solicitar ao usuário o preço de cada fruta.
# - Mantenha uma variável para armazenar o preço total.
# - Adicione o preço de cada fruta ao preço total.
# - Após inserir todos os preços, imprima o preço total.


frutas = []
total = 0

while True:
  fruta = input("Digite o nome da fruta (ou 'sair' para parar): ")
  if fruta == "sair":
    break
  preco = float(input("Digite o preço da fruta: "))
  frutas.append(fruta)
  total += preco

print("Você comprou:", frutas)
print("Preço total:", total)