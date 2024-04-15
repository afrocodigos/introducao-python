#Feito por Gabriel Amaral
numero = int(input("Entre com um número: "))

for i in range(1, numero+1):
    if i % 15 == 0:
        aux = "FIZZBUZZ"
    elif i % 5 == 0:
        aux = "BUZZ"
    elif i % 3 == 0:
        aux = "FIZZ"
    else:
        aux = str(i)
    print(aux)

        
    


