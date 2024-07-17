#Faça um programa que calcule o mostre a média aritmética de N notas.
quanto=int(input("Quantas notas voce quer calcular:"))
media=0
aux=1
for aux in range(quanto):
  nota=float(input("Qual foi sua nota:"))
  media=media+nota

media=media/quanto
print("A media dessas notas é {}".format(media))