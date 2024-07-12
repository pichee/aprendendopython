#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1=int(input("Digite um numero:"))
n2=int(input("Digite outro numero:"))
if n1>n2:
  aux=n1
  n1=n2
  n2=aux
while True:
  if n1<=n2:
    print("{}".format(n1))
    n1=n1+1