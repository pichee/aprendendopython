#Faça um programa que leia 5 números e informe o maior número.
maior=int(input("Digite um numero inteiro:"))
menor=maior
c=0
while c<4:
  numero=int(input("Digite um numero inteiro:"))
  if numero>maior:
    maior=numero
  c=c+1
  
print("O maior numero digitado é {}".format(maior))