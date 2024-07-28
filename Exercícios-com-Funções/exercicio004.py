#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
i=int(input("Digite um numero:"))
def funcao(x):
    if x<0:
        print("Esse numero é negativo")
    else:
        print("Esse numero é positivo")


funcao(i)
