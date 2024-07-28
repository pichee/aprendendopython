##Faça um programa para imprimir:
##    1
##    2   2
##    3   3   3
##    .....
##    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha
variavel=int(input("Digite a quantidade de numeros que voce quer:"))
x=1
def funcao(x):
    aux=1
    while aux<=x:
        print(f"{x} ",end="")
        aux+=1
y=1
variavel=variavel+1
for y in range(variavel):
    x=y
    funcao(x)
    print("\n")
