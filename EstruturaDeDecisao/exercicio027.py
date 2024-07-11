#Uma fruteira está vendendo frutas com a seguinte #tabela de preços:
#                      Até 5 Kg           Acima de 5 #Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por #Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por #Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o #valor total da compra ultrapassar R$ 25,00, #receberá ainda um desconto de 10% sobre este total. #Escreva um algoritmo para ler a quantidade (em Kg) #de morangos e a quantidade (em Kg) de maças #adquiridas e escreva o valor a ser pago pelo #cliente.
#O Hipermercado Tabajara está com uma promoção de #carnes que é imperdível. Confira:

tipo_carne = input("Digite o tipo de carne (file duplo, alcatra, picanha): ").lower()
quantidade = float(input("Digite a quantidade de carne (em Kg): "))
usa_cartao = input("Pagamento com cartão Tabajara? (s/n): ").lower() == 's'

if tipo_carne == "file duplo":
    if quantidade <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif tipo_carne == "alcatra":
    if quantidade <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
elif tipo_carne == "picanha":
    if quantidade <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
else:
    raise ValueError("Tipo de carne inválido")

preco_total = preco_kg * quantidade
desconto = 0
if usa_cartao:
    desconto = preco_total * 0.05

preco_final = preco_total - desconto
tipo_pagamento = "Cartão Tabajara" if usa_cartao else "Dinheiro"

print("---- CUPOM FISCAL ----")
print(f"Tipo de carne: {tipo_carne.capitalize()}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {preco_final:.2f}")
print("----------------------")
