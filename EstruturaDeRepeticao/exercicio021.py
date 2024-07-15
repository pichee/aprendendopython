#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero=int(input("Digite um numero:"))
contador=2
result=1
while contador!=numero:
     result=numero%contador
     if result==0:
      print("Esse numero não é primo")
      exit()
      
     contador=contador+1
 
 
print("esse numero é primo")
