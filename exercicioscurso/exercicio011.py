#faça um programa que leia a largura e a altura de uma parede em metros.Calcule 
#a sua area e a quantidade dee tinta necessaria para pinta-la sabendo que cada litro de tinta
#pinta uma area de 2m
l= float(input("Enther the width:"))
a= float(input("Enter the height:"))
area=l*a
total=area/2
print("If the area is igual {} you need {} liters of paint".format(area,total))
