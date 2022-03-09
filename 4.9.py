
a = float(input("Qual o valor da casa?: "))
b = float(input("Qual o seu salário?: "))
c = int(input("por quantos anos quer pagar?: "))

meses = (c*12) # Quantidade de meses
prest = (a/meses) # Valor mensal
perc30 = (b*0.3) # 30% do salário

if prest > perc30:
    print(" Não aprovado")
    print(f'a mensalidade seria de {prest:5.2f} e 30% do seu salário seria {perc30:5.2f}')
else:
    print(" Aprovado")
    print(f'a mensalidade seria de {prest:5.2f} e 30% do seu salário seria {perc30:5.2f}')