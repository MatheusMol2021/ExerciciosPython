a = int(input("Qual a velocidade do veículo em km/h: "))

if a > 80:
    b = (a - 80) # calcula a velocidade ultrapassada    
    c = (b * 5) #calcula o valor da multa em reais
    print(f"Foi aplicado uma multa de R$ {c:5.2f}")
