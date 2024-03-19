# print("Diga-me sim ou nao")
# resposta = input()
# if resposta == "sim" or  resposta == "s":
#     print("positiva")
# else:
#     print("negativa")

#se o numero for multiplo de 3 print FIZZ if i%3 == 0
#se o numero for multiplo de 5 print BUZZ  elif i%5 == 0
#se nao for multiplo de 3 ou 5 print o numero else 
#se for multiplo de 3 e 5 print FIZZBUZZ elif i%3 == 0 and i%5 == 0

# divisores = [3,5]
# palavras = ["FIZZ", "BUZZ"]
# saida = ""
# numero = int(input("Diga-me um numero: "))

# for i in range(len(divisores)):
#     if (numero % divisores[i]) == 0:
#         saida = palavras[i]
#         print(saida)
#     else:
#         print (numero)
#         break

#numero = int(input("Diga-me um número: ")) 

# numero = 0
# while numero <10:
#     # print (numero)
#     numero = numero+1
for i in range(100):
    if i % 15 == 0:
        print("FIZZBUZZ")
    elif i % 5 == 0:
        print("BUZZ")
    elif i % 3 == 0:
        print ("FIZZ")
    else:
        print(i)

