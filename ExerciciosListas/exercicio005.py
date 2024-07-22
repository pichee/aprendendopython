#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números 
#pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores
vetor=[None]*20
par=[]
impar=[]
a=0
for a in range(20):
 vetor[a]=int(input("Digite um numero:"))
 if vetor[a]%2==0:
   par.append(vetor[a])
 else:
   impar.append(vetor[a])
print(f"a lista {vetor} possui {par} numeros pares e  {impar} como números ímpares")