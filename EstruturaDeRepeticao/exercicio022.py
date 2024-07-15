#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero=int(input("Digite um numero:"))
contador=2
result=1
variavel=1

while contador<numero:
     result=numero%contador
     if result==0:
         print("{}".format(contador))
         variavel=2
     contador=contador+1
         
         
if variavel==1:
         print("numero primo".format(result))