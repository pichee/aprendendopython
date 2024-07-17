#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
numero=int(input("Digite um numero:"))
result=int(1)
aux=int(2)
pula=int(0)
n=2
print("Os numeros primos do 1 ate {}:".format(numero))
for n in range(2,numero+1):
     aux=2
     pula=0
     while aux<n:
        result=n%aux
        if result==0:
         pula=1
         break
        aux=aux+1
         
     if pula==0:
      print("{}".format(n))
     
       
       
    