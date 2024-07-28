#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
i=int(input("Digite um numero:"))
a=0
x=1
def funcao(x):
     y=1
     while y<=x:
      print(f"{y} ",end="")
      y=y+1
i=i+1
while a in range(i):
    x=a
    funcao (x)
    print("\n")
    a=a+1
