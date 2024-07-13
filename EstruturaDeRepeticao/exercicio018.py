#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
conjunto=int(input("Digite até que numero vai teu intervalo:"))
menor=1
maior=conjunto
result=0
for aux in range(conjunto):
    result=result+aux
print("O maior numero desse conjunto é {} o menor é 0 e a soma entre todos os numeros é {}".format(maior,result))
