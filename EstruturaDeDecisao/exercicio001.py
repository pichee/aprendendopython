#Faça um Programa que peça dois números e imprima o maior deles.
numero1=int(input("Digite um numero:"))
numero2=int(input("Digite outro numero:"))
if numero1>numero2:
    print("O numero {:.2f} é maior que {:.2f}".format(numero1,numero2))
if numero2>numero1:
    print("O numero {:.2f} é maior que {:.2f}".format(numero2,numero1))
