#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano=float(input("Digite o ano"))
if ano%100==0 and ano%400:
  print("Isso nao é um ano bissexto")
  exit()
if ano%4==0:
  print("Isso é um ano bissexto")
else:
  print("Isso não é um ano bissexto")