
a = float(input("Qual o valor da dívida?: "))
b = float(input("qual o juro mensal?: "))
c = float(input("Qual o valor pago mensalmente?: "))

x = 1 # contador
y = c


while a > y:
    x = x + 1
    montante = (a * (b/100))
    a = a - c
    
    print(f" O nº de meses será {x-1}")
    print(f"O total pago será {}")
    print(f"total de juros pago é {}")
