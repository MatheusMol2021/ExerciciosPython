

import string


a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = input("Qual o operador matemático (+,-,*,/):")

if c == "+":
    valor = (a+b)
elif c == "-":
    valor = (a-b)
elif c == "*":
    valor = (a*b)
elif c == "/":
    valor = (a/b)
else:
    print("Categoria Inválida, digite entre (+,-,*,/)")
    valor = 0

print(f"o resultado final foi {valor}")