#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
meuVetor =[]
a=0
for a in range(5):
    numero=int(input("Digite um numero:"))
    meuVetor.append(numero)
    
print(f"{meuVetor}")
