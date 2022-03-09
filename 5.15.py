

total = 0
b = 0

while True:
    a = int(input("Digite o código do produto: "))
    if a == 0:
        print(f"o valor total foi {total}")
        break
    elif a == 1:
        b = int(input("Quantidade comprada: "))
        p = 0.5
    elif a == 2:
        b = int(input("Quantidade comprada: "))
        p = 1
    elif a == 3:
        b = int(input("Quantidade comprada: "))
        p = 4
    elif a == 5:
        b = int(input("Quantidade comprada: "))
        p = 7
    elif a == 9:
        b = int(input("Quantidade comprada: "))
        p = 8
    else:
        print("Código inválido")
        p = 0
    temp = (b*p)
    total += temp