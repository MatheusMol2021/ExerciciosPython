
a = float(input("digite o salário R$: "))

if a > 1250:
    b = (a * 1.1)
if a <= 1250:
    b = (a * 1.15)

print(f"O novo salario será R$ {b:6.2f}")