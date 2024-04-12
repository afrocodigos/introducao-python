divisores = [3,5]
palavras = ["FIZZ","BUZZ"]
saida = ""

numero = int(input("Entre com um número: "))

for i in range(len(divisores)):
    if (numero % divisores[i]) == 0:
        saida += palavras[i]

if (saida == ""):
    print(numero)
else:
    print(saida)
    