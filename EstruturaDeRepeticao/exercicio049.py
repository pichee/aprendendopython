#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#Imprima no final a soma da série.
numero_termos=int(input("Quantos termos essa pg vai ter:"))
n1=1
n2=1
soma=0
for a in range(numero_termos):
  soma=(n1/n2)+soma
  if a==numero_termos-1:
    print(f"{n1}/{n2}.",end="")
  else:
     print(f"{n1}/{n2}+",end="")
  n1=n1+1
  n2=n2+2
print(f"\nO resultado dessa pg é {soma}")