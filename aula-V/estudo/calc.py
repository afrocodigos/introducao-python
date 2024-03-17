from operacoes import soma, subtracao, divisao, multiplicacao

primeiro_numero = int(input("Diga me o primeiro numero"))
segundo_numero = int(input("Diga me o segundo numero"))

resultado_soma = soma(primeiro_numero, segundo_numero)
resultado_subtracao = subtracao(primeiro_numero, segundo_numero)
resultado_divisao = divisao(primeiro_numero, segundo_numero)
resultado_multiplicacao = multiplicacao(primeiro_numero, segundo_numero)

print(f"O resultado da soma é: {resultado_soma}")
print(f"O resultado da subtracao é: {resultado_subtracao}")
print(f"O resultado da divisao é: {resultado_divisao}")
print(f"O resultado da multiplicacao é: {resultado_multiplicacao}")

