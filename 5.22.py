
while True:
    print("#"*30)
    print(" MENU ")
    print("Adição = 1 \nsubtração = 2 \ndivisão = 3 \nmultiplicação = 4 \nsair = 5")
    print("#"*30)

    a = int(input("Digite uma das opções do menu acima: "))
    if a == 5:
        break

    tabuada = 1
    print(f"Tabuada de 1")
    while tabuada <= 10:
        numero = 1
        while numero <= 10:
            if a == 1:
                print(f"{tabuada} + {numero} = {tabuada + numero}")
            if a == 2:
                print(f"{tabuada} - {numero} = {tabuada - numero}")
            if a == 3:
                print(f"{tabuada} * {numero} = {tabuada * numero}")
            if a == 4:
                print(f"{tabuada} / {numero} = {tabuada / numero}")
            numero += 1

        print("-"*30)
        if tabuada <10:
            print(f"Tabuada de {tabuada+1}")
        tabuada += 1
