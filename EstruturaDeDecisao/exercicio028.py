#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
kg=float(input("Quantos kg voce comprou:"))
nome=input("O que voce comprou \nMorango[1]\n Maça[2]\n")
vendas=0
if nome>2 or kg<=0:
    print("Compra invalida")
if kg>5 and nome==1:
    vendas=2.20*kg
if  kg<=5 and nome==1:
    vendas=2.50*kg
if  kg<=5 and nome==2:
    vendas=1.8*kg
if  kg>=5 and nome==2:
    vendas=1.5*kg

if vendas>25 or kg>8:
    vendas=vendas-(vendas*0.10)

print("O valor total a pagar é igual {:.2f}".format(vendas))

