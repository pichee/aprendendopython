#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base=int(input("Digite a base:"))
expoente=int(input("Digite o expoente:"))
c=int(0)
res=1

while c<expoente:
  res=res*base
  c=c+1

print("{}".format(res))