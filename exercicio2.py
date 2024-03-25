    
preco_total = 0    
while True:
        preco_fruta = input("Digite o preço da fruta (ou 'fim' para encerrar): ")
        
        if preco_fruta == 'fim':
            break

        try: 
            preco_fruta = float(preco_fruta)
            if preco_fruta >= 0:
                preco_total =+ preco_fruta 
            else:
                print('preco total deve ser maior que 0')  

        except ValueError: 
            print('digite algo que faça sentido ao sistema') 
    return preco_total

print (preco_total) 


