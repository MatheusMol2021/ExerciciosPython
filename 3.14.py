
qkm = int(input("Qual a quantidade de KM percorrida: "))
qdias = int(input("Quantos dias ficou alugado o veículo: "))

custo = ((60*qdias)+(0.15*qkm))

print(f"O custo total a ser pago é de R$ {custo:5.2f}")