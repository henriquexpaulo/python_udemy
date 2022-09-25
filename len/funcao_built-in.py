"""
num1 = input("DIgite um numero: ")
num2 = input("digite outro numero: ")

#isnumeric, isdigit isdecimal
# checar numero positvos (12324234235)

print(num1.isnumeric())
print(num2.isnumeric())
"""

num1 = input("DIgite um numero: ")
num2 = input("digite outro numero: ")

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)

else: 
    print("erro de calculo, digite um numero inteiro")