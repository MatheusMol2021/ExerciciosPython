L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))

x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x}")
        break
    else:
        print(f"{p} não encontrado")
    x += 1

