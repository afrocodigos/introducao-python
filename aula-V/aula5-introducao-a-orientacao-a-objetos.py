# from operacoes import OperacoesMatematicas

# instanciada_operacoes = OperacoesMatematicas()


# import operacoes

# primeiro_numero = int(input("Diga me o primeiro número."))
# segundo_numero = int(input("Diga me o segundo número."))

# resultado_da_soma = instanciada_operacoes.soma(primeiro_numero, segundo_numero)
# print(f"O resultado da soma é: {resultado_da_soma}")

# resultado_da_subtracao = instanciada_operacoes.subtracao(
#     primeiro_numero, segundo_numero
# )
# print(f"O resultado da subtração é: {resultado_da_subtracao}")

# resultado_da_divisao = instanciada_operacoes.divisao(primeiro_numero, segundo_numero)
# print(f"O resultado da divisao é: {resultado_da_divisao}")
# resultado_da_multiplicacao = instanciada_operacoes.multiplicacao(
#     primeiro_numero, segundo_numero
# )
# print(f"O resultado da multiplicação é: {resultado_da_multiplicacao}")


# from animais import Gato, Cachorro

import animais

gato = animais.Gato(patas=4)


print(f"O som do meu gato é: {gato.som()}")
print(f"O nome do meu gato é: {gato.nome}")



nome_do_cachorro = input("Qual o nome do seu cachorro?")

cachorro = animais.Cachorro(patas=3, nome=nome_do_cachorro)
print(f"O som do meu cachorro é : {cachorro.som()}")
print(f"O nome do meu cachorro é: {cachorro.nome}")
