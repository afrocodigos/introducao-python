
lista = [1,2,3,4,5,5,6,7,8,9,9,10]

lista =set(lista)
print(lista) #aqui o resultado está em formato set 
lista1 = list(lista)
print(lista1) #aqui no caso mudamos o valor do resultado que estava em 'set' para 'list' novamente. 

print(50*('--'))

#Uma outra maneira de fazer este procedimento de maneira mais rápida seria em apenas uma linha transformamos em set e depois transformarmos em lista novamente o mesmo parâmetro: 

Lista2 = [1,2,3,3,4,5,6,7,7,5,4,7,8,9,0,1,3,4,5,6,7,]

Lista2 = list(set(Lista2))
print(Lista2)
