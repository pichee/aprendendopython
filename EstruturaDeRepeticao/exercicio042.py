#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos:
# A entrada de dados deverá terminar quando for lido um número negativo.
while True:
  n1=int(input("Digite um numero:"))
  n2=int(input("Digite outro numero:"))
  if n1<0 or n2<0:
      exit()
  if n1>n2:
    aux=n1
    n1=n2
    n2=aux
  while n1<=n2:
    print(f"{n1}")
    n1=n1+1
   