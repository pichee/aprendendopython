
#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor=[]
a=0
for a in range(4):
 numero=float(input("Digite um numero:"))
 vetor.append(numero)

soma=vetor[0]+vetor[1]+vetor[2]+vetor[3]
n=vetor[0]*vetor[1]*vetor[2]*vetor[3]
print(f"Os numeros {vetor} tem soma igual  {soma} e multiplição igual {n}")