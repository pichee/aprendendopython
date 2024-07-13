#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16
numero=17
while numero>16 and numero<0
numero=int(input("Digite o numero fatorial até 16:"))
result=1
print("{}!=".format(numero),end='')
while numero!=0:

    result=result*numero
    print("{}x".format(numero),end='')
    numero=numero-1

print("={}".format(result))
