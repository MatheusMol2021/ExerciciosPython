

while True:
    
    a = input("Difite os parenteses() ou S para sair: ")

    if a == "S":
        break

    x = 0 # conta os índices da pilha
    y = 0 # Conta os parametros à esquerda ou à direita
    while x < len(a):
        if a[x] == "(":
            y += 1
        elif a[x] == ")":
            y -= 1
        x += 1

    if y != 0:
        print("Erro")
    else:
        print("OK")