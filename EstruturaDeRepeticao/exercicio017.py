#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
numero=int(input("Digite o numero fatorial:"))
result=1
print("{}!=".format(numero),end='')
while numero!=0:

    result=result*numero
    print("{}x".format(numero),end='')
    numero=numero-1

print("={}".format(result))
