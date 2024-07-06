#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
produto1=float(input("Qual o valor do primeiro produto"))
produto2=float(input("Qual o valor do segundo produto"))
produto3=float(input("Qual o valor do terceiro produto"))
if produto1==produto2 or produto2==produto3 or produto1==produto3:
   print("nenhum produto pode ter o mesmo preço")
if produto1<produto2 and produto1<produto3:
  print("O produto com o menor valor é {}".format(numero1))
if produto2<produto1 and produto2<produto3:
  print("O produto com o menor valor é {}".format(numero2))
if produto3<produto2 and produto3<produto1:
  print("O produto com o menor valor é {}".format(numero3))