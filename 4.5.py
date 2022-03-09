
a = float(input("digite o salário R$: "))

if a > 1250:
    b = (a * 1.1)
if a <= 1250:
    b = (a * 1.15)

print(f"O novo salario pelo IF será R$ {b:6.2f}")

if a > 1250:
    b = (a * 1.1)
else:
    b = (a * 1.15)

print(f"O novo salario pelo ELSE será R$ {b:6.2f}")