"""Faça um programa que liste para o usuário um menu
com quatro opções, sendo cada uma referente à uma operação matemática básica.
Após o usuário ter escolhido a opção, leia dois valores e realiza a operação selecionada.
"""
while True:

    print("")
    print("-------calculadora--------")
    print("---operadores matematico---")
    print("")
    print("uma calculadora operadores de +, -, *, /")
    print("")
    print("digite 1 pra +")
    print("digite 2 pra -")
    print("digite 3 pra *")
    print("digite 4 pra /")
    print("digite 5 pra sair")

    operadormat = int(input("Digite uma opçao: "))

    if operadormat >=5:
        break

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("")

    if operadormat == 1:    
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
        break
    elif operadormat == 2:
        print(f"{valor1} - {valor2} = {valor1 - valor2}")
        break
    elif operadormat == 3:
        print(f"{valor1} * {valor2} = {valor1 * valor2}")
        break
    elif operadormat == 4:
        print(f"{valor1} / {valor2} = {valor1 / valor2:.2f}")
        break
    else: 
        print("Opçao invalida")