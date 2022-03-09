
a = float(input("Qual o deósito inicial?: "))
b = float(input("qual a taxa de juros?: "))
c = float(input("Qual o valor depositado mensalmente?: "))

x = 1 # contador
y = a # acumulador

while x <= 24:
    x = x + 1
    y = y + (y * (b/100)) + c
    print(f" O mês {x-1} terá valor de {y:5.2f}")
