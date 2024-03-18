def ola_pessoa(nome = "mundo"):
    print(f"Olá, {nome}!")


print("Exemplo de função que não precisa de um valor de entrada")

nome_usuario = input("Qual o seu nome? ")
ola_pessoa(nome_usuario)
ola_pessoa()
