#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
c=0
while c<50:
  c=c+1
  if c%2==1:
    print("{}".format(c))