multiplos = int(input("Diga me um número: "))  # o python espera uma entradas do usuário

divisoes = (3, 5, 15)

range() # gera uma lista de números 
for indice, elemento in enumerate(divisoes): # 15
    print(indice, elemento)

# laço de repetição while
contador = 0
while contador < 11:
    contador = contador + 1 # count = count + 1
    print(contador)

# Se a entrada for 15 eu deveria ter uma saída como abaixo
# 1
# 2
# FIZZ
# 4
# BUZZ
# FIZZ
# 7
# 8
# FIZZ
# 10
# 11
# FIZZ
# 13
# 14
# FIZBUZZ




# if multiplos % 15 == 0:
#     print("FIZZBUZZ")

# elif multiplos % 5 == 0:
#     print("BUZZ")

# if multiplos % 3 == 0:
#     print("FIZZ")
# else:
#     print(multiplos)


# se numero for multiplo de 3 print FIZZ. Múltiplo de 3: 6 % 3 == 0
# se número for múltiplo de 5 print BUZZ
# se número for múltiplo de 5 e de 3 print FIZZBUZZ
# se não for múltiplo de 3 nem de 5 imprime o próprio número
