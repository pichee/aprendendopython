#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
a=float(input("Digite o valor de a:"))
if a==0:
  print("A equação não é do segundo grau")
  exit()
b=float(input("Digite o valor de b:"))
c=float(input("Digite o valor de c:"))
delta=(-b*2)-(4*a*c)
delta=math.sqrt(delta)
resultadopositivo=(-b+delta)/(2*a)
resultadonegativo=(-b-delta)/(2*a)
if delta==0:
  print("A equacão apresenta apenas um resultado que é {}".format(resultadopositivo))
  exit()
print("As raizes apresentam 2 valores {} e {}".format(resultadopositivo,resultadonegativo))