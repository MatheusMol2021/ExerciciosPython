
a = int(input("Digito primeiro numero: "))
b = int(input("digite o segundo número: "))


x = 1 #contador
a1 = a # Valor inicio

while a1 >= b:
    x = x + 1
    a1 = (a1 - b)

    resto = (a1)

print(f'O resultado foi {x-1}')
print(f'o resto da divisão é {resto}')