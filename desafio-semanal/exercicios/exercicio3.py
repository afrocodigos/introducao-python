# Crie um programa que ordene uma lista de frutas em ordem alfabética.

# Dicas que podem ser seguidas ou não: 
# - Use o método sort() para ordenar a lista em ordem alfabética.
# - Certifique-se de usar o argumento key=str.lower para que a ordenação seja case-insensitive.


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Primeiro, solicitei a quantidades de frutas que usuário deseja ordenar
quantidade = int(input(f"Digite a quantidade de frutas que você deseja ordenar: "))
print()

#Também, criei uma lista para armazenar o nome das frutas que será colocado pelo usuário.
frutas_personalizadas = []

#O loop irá executar o número de vezes especificado pela variável quantidade.
for i in range(quantidade):
    fruta = input(f"Digite o nome da fruta {i+1} ou pressione Enter para parar: ")
    if fruta == "":
        break
    frutas_personalizadas.append(fruta)

#Agora, utlizei o "sort" para colocar em ordem alfabética e o "key=str.lower" que faz com que a ordenação seja case-insensitive.
frutas_personalizadas.sort(key=str.lower)

print("Sua lista de frutas personalizada em ordem alfabética (case-insensitive) é:", frutas_personalizadas)
