
s = 0
x = 0

while True:
    v = int(input('Digite um número para somar e 0 para sair: '))
    if v == 0:
        break
    s += v
    x += 1

print(f'A quantidade toal somada foi {s}')
print(f'A Quantidade de números foi {x}')
