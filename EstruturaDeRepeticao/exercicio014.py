#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
contp=int(0)
conti=int(0)
for i in range(10):
  numero=int(input("Digite um numero:"))
  if numero%2==0:
    contp=contp+1
  else:
    conti=conti+1
print("O numero de numeros pares é {} e o numero de numeros impar é {}".format(contp,conti))