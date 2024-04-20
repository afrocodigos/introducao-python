print("Digite um numero");
meu_numero = int(input());

def fizzbuzz(numero):
    for num in range(1, numero+1):
        if num % 15 == 0:
            print("fizzbuzz");
        elif num % 3 == 0:
            print("fizz");
        elif num % 5 == 0:
            print("buzz");
        else:
            print(num);

fizzbuzz(meu_numero);