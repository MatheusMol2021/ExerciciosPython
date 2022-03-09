
a = int(input("Qual a distancia que deseja percorrer?: "))

if a <= 200:
    b = (a * 0.5)
else:
    b = (a * 0.45)

print(f"O custo da passagem total será R$ {b:5.2f}.")