

a = int(input("Qual a quantidade de kWh consumida?: "))
b = input("Qual o tipo de instalação (R,C,I):") # Residencial, Comercial ou Industrial

if b == "R":
    if a <= 500:
        custo = (a*0.4)
    else:
        custo = (a*0.65)
elif b == "C":
    if a <= 1000:
        custo = (a*0.55)
    else:
        custo = (a*0.6)
elif b == "I":
    if a <= 5000:
        custo = (a*0.55)
    else:
        custo = (a*0.6)
else:
    print ("Tipo de fornecimento inválido")
    custo = 0

print(f'o Custo total foi {custo:5.2f}')