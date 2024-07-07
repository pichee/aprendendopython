#Faça um Programa que leia três números e mostre-os em ordem decrescente.
numero1=float(input("Digite um numero:"))
numero2=float(input("Digite um numero:"))
numero3=float(input("Digite um numero:"))
if numero1==numero2 or numero1==numero3 or numero3==numero2:
    print("Não coloque números iguais")
if numero2>numero1 and numero2>numero3 and numero1<numero3:
    print("A ordem decrescente é {},{},{}".format(numero2,numero1,numero3))
if numero2>numero1 and numero2>numero3 and numero3<numero1:
    print("A ordem decrescente é {},{},{}".format(numero2,numero3,numero1))
if numero3>numero1 and numero3>numero2 and numero1<numero2:
    print("A ordem decrescente é {},{},{}".format(numero3,numero1,numero2))
if numero3>numero1 and numero3>numero2 and numero2<numero1:
    print("A ordem decrescente é {},{},{}".format(numero3,numero1,numero2))
if numero1>numero3 and numero1>numero2 and numero2<numero3:
    print("A ordem decrescente é {},{},{}".format(numero1,numero2,numero3))
if numero1>numero3 and numero1>numero2 and numero3<numero2:
    print("A ordem decrescente é {},{},{}".format(numero1,numero3,numero2))
