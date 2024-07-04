# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n=int(input("Enter any angle:"))
cos=math.cos(math.radians(n))
tan=math.tan(math.radians(n))
sen=math.sin(math.radians(n))
print("The cosseno is igual{:.2f}\nThe tangente is igual {:.2f}\nAnd the seno is igual{:.2f}".format(cos,tan,sen))
