from operacoes import soma, subtracao, multiplicacao, divisao

primeiro_numero = int(input("Por favor, insira o primeiro número: "))
segundo_numero = int(input("Por favor, insira o segundo número: "))

print(f"O resultado da soma entre {primeiro_numero} e {segundo_numero} é {soma(primeiro_numero,segundo_numero)}")
print(f"O resultado da subtração entre {primeiro_numero} e {segundo_numero} é {subtracao(primeiro_numero,segundo_numero)}")
print(f"O resultado da multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicacao(primeiro_numero,segundo_numero)}")
print(f"O resultado da divisão entre {primeiro_numero} e {segundo_numero} é {divisao(primeiro_numero,segundo_numero)}")
