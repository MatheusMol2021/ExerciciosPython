
a = float(input("Qual o deósito inicial?: "))
b = float(input("qual a taxa de juros?: "))

x = 1 # contador
y = a # acumulador

while x <= 24:
    x = x + 1
    y = y + (y * (b/100))
    print(f" O mês {x-1} terá valor de {y:5.2f}")
