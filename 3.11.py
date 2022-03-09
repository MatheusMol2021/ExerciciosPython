
preco = int(input("Qual o preço da mercadoria (R$): "))
desc = int(input("Qual o percentual de desconto (%): "))

valor_desc = (preco * (desc/100))
valor_merc = (preco - valor_desc)

print(f"o valor descontaado é de R$ {valor_desc:5.2f}, portanto")
print(f'o valor a ser pago é de R$ {valor_merc:5.2f}')