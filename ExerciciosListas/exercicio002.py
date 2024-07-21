#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
meuVetor =[]
a=0
for a in range(10):
    numero=int(input("Digite um numero:"))
    meuVetor.append(numero)
    
vetorinv=meuVetor[::-1]
print(f"{vetorinv}")
