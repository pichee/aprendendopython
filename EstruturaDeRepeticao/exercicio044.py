#Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
#1 , 2, 3, 4  - Votos para os respectivos candidatos 
#(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco
#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
while True:
  print("ELEIÇÃO:\nJosé[1]\nPascal[2]\nCristiano Ronaldo[3]\nFarofa[4]\nNulo[5]\nBranco[6]")
  voto=int(input("Digite o seu voto:"))
  if voto==1:
    c1=c1+1
  if voto==2:
    c2=c2+1
  if voto==3:
    c3=c3+1
  if voto==4:
    c4=c4+1
  if voto==5:
    c5=c5+1
  if voto==6:
    c6=c6+1
  algo=input("Tem mais alguem para votar sim[s] ou não[n]")
  if algo=="n":
    break
print(f"Resultado eleição:\nJose{c1}\nPascal{c2}\nCristiano Ronaldo{c3}\nfarofa{c4}\nnulo{c5}\nbranco{c6}")
  