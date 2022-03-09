salario = float(input("Escreva o valor do salário (R$): "))
percentual = int(input("Qual o percentual de aumento (%): "))

salario2 = (salario + (salario * (percentual/100)))
aumento = salario2-salario


print(f'o novo slário é R$ {salario2:5.2f}')
print(f'O aumento foi de R$ {aumento:5.2f}')