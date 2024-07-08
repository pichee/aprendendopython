#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
 # Entre 9.0 e 10.0        A
 # Entre 7.5 e 9.0         B
 # Entre 6.0 e 7.5         C
 # Entre 4.0 e 6.0         D
 # Entre 4.0 e zero        E  
  
  nota1=float(input("Digite sua primeira nota:"))
  nota2=float(input("Digite sua segunda nota:"))
  media=(nota1+nota2)/2
  if media<=4 and media>0:
    print("Sua nota é E voce nao foi aprovado")
  if media>4 and media<=6:
    print("Sua nota é D voce nao foi aprovado")
  if media>6 and media<=7.5:
    print("Sua nota é C voce foi aprovado")
  if media>7.5 and media<=9:
    print("Sua nota é B voce foi aprovado")
  if media>9 and media<=10:
    print("Sua nota é A voce foi aprovado")
  if media>10 or media<0:
    print("Nota nao valida")