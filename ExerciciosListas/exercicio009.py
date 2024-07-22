#Faça um Programa que leia um vetor A com 10 
#números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
vetor=[9]
a=0
for a in range(9):
  numero=float(input("Digite um numero:"))
  vetor.append(numero*numero)
print(f"A raiz quadrada desses numeros é {vetor}")