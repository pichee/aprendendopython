#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
aluno=int(input("Digite a altura do aluno 1:"))
maior=aluno
menor=aluno
c=1
cm=1
for a in range(9):
  aluno=int(input("Digite a altura do aluno {}:".format(a+2)))
  if aluno>maior:
    maior=aluno
    c=a
  if aluno<menor:
    menor=aluno
    cm=a
print("O maior aluno é o {} com {}\nE o menor aluno é o {} com {}".format(c,maior,cm,menor))