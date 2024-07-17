#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
cds=int(input("Quantos cds voce tem:"))
media=0
maximo=0
for a in range(cds):
  valor=float(input("Quanto voce gastou no {} cd:".format(a+1)))
  maximo=maximo+valor
  media=media+valor
  
media=media/cds
print("O valor total gasto foi {:.2f} e a media foi {:.2f}".format(maximo,media))
  