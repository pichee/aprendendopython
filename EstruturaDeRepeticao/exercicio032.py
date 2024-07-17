#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
fatorial=int(input("Digite um numero:"))
print("{}!={}x".format(fatorial,fatorial),end="")
aux=fatorial-1
while aux>0:
   fatorial=fatorial*aux
   if aux!=1:
    print("{}x".format(aux),end="")
    aux=aux-1
   else:
       print("{}=".format(aux),end="")
       aux=aux-1
    
print("{}".format(fatorial))