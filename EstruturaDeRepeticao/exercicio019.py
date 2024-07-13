#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
conjunto=0
while conjunto>1000 and conjunto<1:
conjunto=int(input("Digite até que numero vai teu intervalo de 1 a 1000:"))
menor=1
maior=conjunto
result=0

for aux in range(conjunto):
    result=result+aux
print("O maior numero desse conjunto é {} o menor é 0 e a soma entre todos os numeros é {}".format(maior,result))
