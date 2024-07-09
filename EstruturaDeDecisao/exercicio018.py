#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia=int(input("Digite o dia:"))
mes=int(input("Digite o mes:"))
ano=int(input("Digite o ano:"))
if dia>31 or dia<1 or mes>12 or mes<1 or ano<0:
  print("Data invalida")
else:
  print("Data valida")