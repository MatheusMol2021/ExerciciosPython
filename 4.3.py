"""
salário = float(input("Digite o salário para cálculo de imposto: "))
base = salário
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000)* 0.20)

print(f"O salário: R${salário:6.2f} Imposto a pagar: R$ {imposto:6.2f}")
"""

a = int(input("digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

if a >= b and a >= c:
    mai = a
if a <= b and a <= c:
    men = a
if b >= c and b >= a:
    mai = b
if b <= c and b <= a:
    men = b
if c >= a and c >= b:
    mai = c
if c <= a and c <= b:
    men = c

print(f"o maior valor é {mai} e o menor é {men}")