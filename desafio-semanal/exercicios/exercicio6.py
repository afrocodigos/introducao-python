import pandas as pd
from datetime import datetime
from pytz import timezone

def verificar_cupom(cupom):

    if cupom.lower() == "olabi":
        
        desconto_percentual = 10
        return desconto_percentual
    else:
        return 0

frutas_unicas = []


df = pd.DataFrame(columns=["Nome", "Data", "Frutas", "Preço Total"])

while True:
    nome = input("Insira seu nome: ")
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('America/Sao_Paulo')
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

    frutas = []
    preco_total = 0

    while True:
        fruta = input("Insira o nome da fruta (ou 'fim' para parar): ")
        if fruta == "fim":
            break
        frutas.append(fruta)

        if fruta not in frutas_unicas:
            frutas_unicas.append(fruta)

        preco = float(input("Insira o preço da fruta: "))
        preco_total += preco

    df_temp = pd.DataFrame({"Nome": [nome], "Data": [data_e_hora_em_texto], "Frutas": [frutas], "Preço Total": [preco_total]})

    df = pd.concat([df, df_temp], ignore_index=True)

    cupom = input("Insira o cupom de desconto (ou deixe em branco): ")
    desconto = verificar_cupom(cupom)
    if desconto > 0:
        valor_com_desconto = preco_total - (preco_total * desconto_percentual / 100)
        print(f"Desconto aplicado: {desconto:.2f}% valor com desconto R$ {valor_com_desconto:.2f}")

    continuar = input("Deseja inserir mais dados? (s/n): ")
    if continuar == "n":
        break

df.to_csv("dados_frutas.csv", index=False)

print("\nLista de frutas únicas:")
for fruta in frutas_unicas:
    print(fruta)
