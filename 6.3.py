
l1 = []
l2 = []
l3 = []
l4 = []

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

l3 = l1 + l2


x = 0
while x < len(l3):
    y = 0
    while y < len(l4):
        if l3[x] == l4[y]:
            break
        y += 1
    if y == len(l4):
        l4.append(l3[x])
    x += 1
x = 0

print(l1)
print(l2)
print(l3)
print(l4)