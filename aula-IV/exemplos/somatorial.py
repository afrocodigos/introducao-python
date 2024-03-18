def somatorio(num=1):
    if num>1:
        soma_final = num + somatorio(num-1)
    else:
        soma_final = 1

    return soma_final

numero_entrada = int(input("Insira um número: "))

resultado = somatorio(numero_entrada)

print(f"O número inserido foi {numero_entrada}. O resultado da somatória foi {resultado}")