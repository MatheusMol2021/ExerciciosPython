
último = 10
último2 = 10
fila = list(range(1, último + 1))
fila2 = list(range(1, último2 + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila 1")
    print(f"Fila 1 atual: {fila}")
    print(f"Existem {len(fila2)} clientes na fila 2")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F,G para adicionar um cliente ao fim da fila ")
    print("ou A, B para realizar o atendimento. S para sair. ")
    operação = input("Operação (F, G, A, B ou S): ")

    x = 0
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        if operação[x] == "B":
            if len(fila) > 0:
                atendido2 = fila2.pop(0)
                print(f"Cliente {atendido2} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")


        elif operação[x] == "F":
            último += 1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "G":
            último2 += 1 # Incrementa o ticket do novo cliente
            fila2.append(último2)

        elif operação[x] == "S":
            break
        else:
            print("Operação inválida! Digite F, A ou S!")
        x +=1
