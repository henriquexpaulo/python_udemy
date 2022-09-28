#len= define um limete de caracteres, nao funciona em float e int

usuario = input("Digite seu nome: ")
tamanho = len(usuario)

print(f"seu nome tem o total de letras é {tamanho}")

if tamanho >= 6:
    print("seu usuario foi cadastrado")
else:
    print("letras insuficiente para o cadastramento")
