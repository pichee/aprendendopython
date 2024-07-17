#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
quantidade=int(input("Quantos estudantes a turma tem:"))
media=float(0)
c=1
for a in range(quantidade):
 idade=int(input("Quantos anos tem o {}⁰ estudante:".format(c)))
 c=c+1
 media=media+idade
media=media/quantidade
if media<=25:
  print("A media {} classifica a turma como jovem".format(media))
elif media>=26 and media<=60:
  print("A media {} classifica a turma como Adulta".format(media))
else:
  print("A media {} classifica a turma como Idosa".format(media))