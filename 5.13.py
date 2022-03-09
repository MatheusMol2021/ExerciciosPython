
# a = float(input("Qual o valor inicial da dívida? :"))
a = 2000.00
# b = float(input("Qual a taxa mensal de juros?: "))
b = 1
# c = float(input("Qual o valor mensal que será pago?: "))
c = 100.00

divida = (a + (a * (b/100)))
meses = 0
juros = 0

while divida > 0:
    meses = meses + 1
    juros = (juros+(divida * (b/100)))
    divida = ((divida + (divida * (b/100))) - c)


print(f'A quantidade de meses foi {meses} meses')
print(f'O valor total de juros foi de R${juros:5.2f}')
