#Faça um programa que leia 5 números e informe a soma e a média dos números.
media=0
c=0
while c<5:
  numero=float(input("Digite um numero:"))
  c=c+1
  media=media+numero

  
media=media/5
print("A media desses 5 numeros é {}".format(media))