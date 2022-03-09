
qcig = int(input(" Qual a quantidade de cigarros fumados por dia: "))
qanos = int(input("Quanto anos já fumou: "))

total_cig = (qanos*365)*qcig
total_tempo = (total_cig*10)
tempo_dias = int((total_tempo/60)/24) 

print(f"O fumante perdeu {tempo_dias} dias de vida")