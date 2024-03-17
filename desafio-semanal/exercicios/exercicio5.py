# Crie um programa que calcule o preço final de um produto após aplicar um desconto percentual fornecido pelo usuário.

# Dicas que podem ser seguidas ou não: 
# - Solicite ao usuário o preço original do produto e o desconto percentual ou armazene esses valores sem o input.
# - Calcule o preço final aplicando o desconto percentual ao preço original.
# - Imprima o preço final.
from descontos import OperacoesProdutos

instanciando_operacoes = OperacoesProdutos()

produtos = int(input("Digite quantos produtos você quer: "))
preco = float(input("Preço dos produtos: "))
desconto = float(input("Desconto em porcentagem: "))

total_a_pagar = instanciando_operacoes.valortotal(produtos,preco)
pagar_com_desconto = instanciando_operacoes.descontoproduto(total_a_pagar,desconto)
valor_com_desconto = instanciando_operacoes.valorfinal(total_a_pagar,pagar_com_desconto)

print(f"Total a pagar sem Desconto: {total_a_pagar}")
print(f"Valor do desconto: {pagar_com_desconto}")
print(f"Total a pagar com Desconto: {valor_com_desconto}")