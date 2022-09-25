#acesso ao um portao de um predio

ap = input("Digite sua senha do ap: ")
morador = input("Seu nome: ")

ap1 = "12345"
nome_morador = "paulo"

if ap1 == ap and nome_morador == morador:
    print("Acesso liberado")
else:
    print("senha invalida, acesso negado")
