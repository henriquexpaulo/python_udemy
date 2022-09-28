from unittest import case


usuario = input("Nome de usuário: ")
senha = input("Senha do usuário: ")

usuario_bd = "paulo"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("voce acessou o sistema")
else:
    print("Usuario ou senha invalido")
