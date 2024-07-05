#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
numero1=int(input("Digite um numero inteiro:"))
numero2=int(input("Digite outro numero inteiro:"))
numeroreal=float(input("Digite um numero flutuante:"))
calculo1=numero1*2+numero2/2
calculo2=numero1*3+numeroreal
calculo3=numeroreal*numeroreal*numeroreal
print("{}\n{}\n{}\n".format(calculo1,calculo2,calculo3))