#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganhar=float(input("Quanto voce ganha por hora?"))
horas =float(input("Quantas horas inteiras voce trabalhou?"))
ganhar=ganhar*horas
print("trabalhando {} horas voce vai ganhar {:.2f}Rs".format(horas,ganhar))