#Altere o programa anterior para mostrar no final a soma dos números.
n1=int(input("Digite um numero:"))
n2=int(input("Digite outro numero:"))
if n1>n2:
  aux=n1
  n1=n2
  n2=aux

while n1<=n2:
  if n1<=n2:
    print("{}".format(n1))
    n1=n1+1
    
soma=n1+n2
print("e a soma entre esses 2 numeros é igual a {}".format(soma))
