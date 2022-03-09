
l1 = []
l2 = []

while True:
    a = int(input("Digite um número para L1 ou 0 para sair: "))
    if a == 0:
        break
    l1.append(a)
while True:
    a = int(input("Digite um número para L2 ou 0 para sair: "))
    if a == 0:
        break
    l2.append(a)

l3 = l1+l2
print(l3)
