#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
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
  n1=1
  n2=n2+1
print(f"\nO resultado dessa pg é {soma}")