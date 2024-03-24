# somatorio
# somatorio(5)
# retornar a soma de 5 + 4 + 3 + 2 + 1 = 15

def somatorio(num):
    sum = 0;
    for i in range(0, num+1):
        if(num == 0 or num == 1):
            return 1;
        sum += i;
    return sum;

print("insira um numero para somar");
numero = int(input());
print(f"O resultado da soma é: {somatorio(numero)}");