lista_de_frutas = []
quantidade = int(input("Me diga quantas frutas você deseja inserir na lista?"))

for i in range (quantidade): 
   a = str(input(f'Fale uma fruta a ser {i + 1} inserida na lista'))
   lista_de_frutas.append(a)
print(lista_de_frutas)


#descrevendo nossa função: 
def ordenamento (frutas):
   frutas.sort(key=str.lower)
               

ordenamento(lista_de_frutas)
print(lista_de_frutas)