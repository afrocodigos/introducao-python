# Crie um programa que conte quantas vezes cada tipo de fruta aparece em uma lista.

# Dicas que podem ser seguidas ou não: 
# - Utilize um dicionário para armazenar o número de ocorrências de cada fruta.
# - Passe pela lista e incremente o valor do dicionário para cada fruta encontrada.
# - No final, imprima o dicionário.

#Resposta


def contagem_frutas(lista_frutas):
  
  armazenamento_frutas = {}
  
  for frutas in lista_frutas:
    
    if frutas in armazenamento_frutas:
      armazenamento_frutas[frutas] += 1
      
    else:   
      armazenamento_frutas[frutas] = 1
      
  return armazenamento_frutas
      
lista_frutas = ["banana", "tomate", "maçã", "pera", "banana", "manga", "maçã", "manga", "pera"]   


resultado = contagem_frutas(lista_frutas)
 
    #dicionário
for fruta, quantidade in resultado.items():
  print(f"{fruta}: {quantidade}")
  
  
#usando o método .items(), que retorna uma sequência de tuplas (chave, valor) representando cada par chave-valor no dicionário.
#no dicionario estamos usando a atribuição multipla.
#print: vai aparece fruta tal: e a quantidade que tem dela.