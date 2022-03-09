
dias = int(input("Escreva quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))

# 1 dia tem 86400 segundos
dias1 = (dias * 86400)
# 1 hora tem 3600 segundos
horas1 = (horas * 3600)
# 1 minuto tem 60 segundos
minutos1 = (minutos * 60)

total = (dias1 + horas1 + minutos1 + segundos)
print(f"O total em segundos é: {total}")