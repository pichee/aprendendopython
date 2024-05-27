# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co=float(input("Enter the size the cateto oposto:"))
ca=float(input("Enter the size the cateto adjacente:"))
h=(co*co)+(ca*ca)
h=math.sqrt(h)
print("The hipotenusa is igual {:.2f}".format(h))
