#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
d=int(input("How many days the car was rent:"))
km=float(input("How km he range:"))
d=d*60
km=km*0.155
km=km*d
print("The final value is {}".format(km))
