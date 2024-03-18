# AfroCódigos 2024
# Autora: Alfa Marine

# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Algumas funções utilizadas aqui são as mesmas utilizadas nos exercícios anteriores
# Cria função que remove duplicatas (exercício 1)
def remove_duplicata(lista_entrada):
  lista_saida = []
  lista_duplicatas = []

  for elemento in lista_entrada:
    if elemento in lista_saida:
      lista_duplicatas.append(elemento)
    else:
      lista_saida.append(elemento)

  return lista_saida

# Cria função que ordena lista (exercício 3)
def ordena_lista(lista_entrada):
    lista_saida = sorted(lista_entrada, key=str.lower)
    return lista_saida

# Cria função que conta as frutas e devolve um dicionário contendo fruta: quantidade
def conta_frutas(lista_frutas):    
    frutas = remove_duplicata(lista_frutas)
    frutas_ordenadas = ordena_lista(frutas)
    dict_frutas = {}

    for fruta in frutas_ordenadas:
        dict_frutas[fruta] = lista_frutas.count(fruta)

    return dict_frutas


# Testa a função de contar quantidade de vezes que uma fruta aparece na lista
lista_entrada_frutas = ["melancia","maçã","uva","melancia",
                        "banana","morango","banana","uva",
                        "melancia","maçã","limão","abacaxi"]
dict_quantidade_frutas = conta_frutas(lista_entrada_frutas)

print(f"Lista de frutas original: {lista_entrada_frutas}")
print(f"Quantidade de cada fruta: {dict_quantidade_frutas}")
