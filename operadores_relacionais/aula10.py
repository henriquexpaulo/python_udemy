"""
operadores relacionais  -  aula 4
== igualdade
>= maior que ou igual a
< menor que
>maior que
<= menor que ou igual a
!= diferente
"""

nome = input("Qual o seu nome? ")
idade = input("Qual sua idade? ")

idade = int(idade)


#limite pra pegar um empresitmo 
idade_menor = 20
idade_maior = 30 

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar o emprestimo")
else:
    print(f"{nome} nao pode pegar o emprestimo")