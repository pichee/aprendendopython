#Faça um Programa que leia dois vetores com 10 elementos
#cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores
valor1=[]
valor2=[]
valor3=[]
valor4=[]
a=0
for a in range(9)
 numero1=int(input("Digite um numero:"))
 numero2=int(input("Digite um numero:"))
 numero3=int(input("Digite um numero:"))
 valor1.append(numero1)
 valor2.append(numero2)
 valor3.append(numero3) 
 valor4.append(numero1)
 valor4.append(numero2)
 valor4.append(numero3)  
a=0
 print(f"{valor4}")
  
