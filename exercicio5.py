def preco_final (preco):
    Valor_descontado = preco - percentual_desconto*preco 

    return Valor_descontado

if __name__ == "__main__":
    percentual_desconto = float(input('Qual o valor percentual de desconto em decimais' ))
    preco = float(input('Qual o valor do produto?'))
    Valor = preco_final(preco)
    print(f'O Valor do produto é de: R${Valor}')