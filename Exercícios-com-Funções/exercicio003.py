#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def funcao(x,y,z):
    soma=x+y+z
    print(f"{soma}")
x=int(input("Digite o valor de x:"))
y=int(input("Digite o valor de y:"))
z=int(input("Digite o valor de z:"))

funcao(x,y,z)
