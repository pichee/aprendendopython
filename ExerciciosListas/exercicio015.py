#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
notas=[]
c=0
while True:
  numero=int(input("digite um numero:"))
  if numero<0:
    break
  else:
    notas.append(numero)
    c+=1
print(f"Notas:{notas}")
print(f"Ao contrario {notas[::-1]}")

soma=sum(notas)
print(f"A soma das notas é {soma}")
media=soma/c
print(f"A media das notas é {media}")
print("Notas acima da media:")
for a in range(len(notas)):
 if notas[a]>=media:
   print(f"{nota[a]}")
a=0
print("Notas abaixo da media:")
for a in range(len(notas)):
 if notas[a]<media:
   print(f"{nota[a]}")
  