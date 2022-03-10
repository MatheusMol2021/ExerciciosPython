L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite o valor a procurar: "))

z = 0

x = 0
while x < len(L):
    if z >= 2:
        break
    elif L[x] == p:
        z += 1
        print(f"{z}º {p} achado na posição {x}")
    elif L[x] == v:
        z += 1
        print(f"{z}º {p} achado na posição {x}")
    else:
        print(f"{p} não encontrado")
    x += 1

