
def contador_frutas (lista_frutas):
        Biblioteca_de_contagem = {} 

        for fruta in lista_frutas: 
                if fruta in Biblioteca_de_contagem:  
                    Biblioteca_de_contagem[fruta] += 1 
                
                else: 
                    Biblioteca_de_contagem[fruta] = 1 
        return Biblioteca_de_contagem

if __name__ == "__main__":
       lista_frutas = ['abacaxi', 'maca', 'banana', 'pera' , "tamarindo"]
       contagem = contador_frutas(lista_frutas)

print("A contagem é de:")
for fruta, quantidade1 in contagem.items():
    print (f'{fruta} : {quantidade1}')

