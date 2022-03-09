
a = int(input("Digite um número: "))

nlido = a
resto = a % 2

if a == 0:
    print("Número não primo")
elif a == 1:
    print("Número não primo")
elif a == 2:
    print("Número Primo")
elif resto == 0:
    print("Número não primo")
else:
    teste = 3
    while