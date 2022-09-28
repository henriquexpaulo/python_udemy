"""Faça um programa que liste para o usuário um menu
com quatro opções, sendo cada uma referente à uma operação matemática básica.
Após o usuário ter escolhido a opção, leia dois valores e realiza a operação selecionada. # noqa: E501
"""

while True:

    print("")
    print("-------Calculadora--------")
    print("---Operadores matematicos---")
    print("")
    print("Operadores de Soma, Subtracao, Multiplicacao, Divisao.")
    print("")
    print("""
    Digite 1 pra Soma(+)
    Digite 2 pra Subtracao(-)
    Digite 3 pra Multiplicacao(*)
    Digite 4 pra Divisao(/)
    """)

    operadormat = int(input("Digite uma opçao: "))

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    print("")

    if operadormat == 1:
        print(f"Valores {valor1} + {valor2} = {valor1 + valor2}")
        break
    elif operadormat == 2:
        print(f"Valores {valor1} - {valor2} = {valor1 - valor2}")
        break
    elif operadormat == 3:
        print(f"Valores {valor1} * {valor2} = {valor1 * valor2}")
        break
    elif operadormat == 4:
        print(f"Valores {valor1} / {valor2} = {valor1 / valor2:.2f}")
        break
    else:
        print("Opçao invalida, tente novamente!")
