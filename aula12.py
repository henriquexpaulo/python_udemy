#len= define um limete de caracteres, nao funciona em float e int

usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("voce precisa digitar pelo menos 6 caracteres")
else:
    print("Voce foi cadastrado no sistema")