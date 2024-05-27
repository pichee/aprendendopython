# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira
import math
n= float(input("Enter a number:"))
print("The value is {} but your part int is {:.0f}".format(n,math.trunc(n)))
