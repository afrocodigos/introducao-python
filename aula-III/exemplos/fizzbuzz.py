print("Por favor, insira um número: ")

numero = int(input())
multiplo_3 = numero%3
multiplo_5 = numero%5


if multiplo_3 == 0 and multiplo_5 == 0:
    print("FIZZBUZZ")
elif multiplo_3 == 0:
    print("FIZZ")
elif multiplo_5 == 0:
    print("BUZZ")
else:
    print(numero)

