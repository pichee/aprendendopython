#Foram anotadas as idades e alturas de 30 
#alunos. 
#Faça um Programa que determine quantos alunos 
#com mais de 13 anos possuem altura inferior 
#à média de altura desses alunos."
alturas=[]
contador=[]
soma=0
idades=[]
a=0
for a in range(2):
  altura=float(input(f"Qual é a altura do aluno {a+1}:"))
  idade=int(input(f"Qual é a idade do aluno {a+1}:"))
  alturas.append(altura)
  contador.append(a)
  idades.append(idade)
  soma=soma+altura
soma=soma/len(contador)
a=0
print("Alunos con mais de 13 anos que possuem altura inferior à média de altura da turma")
for a in range(len(contador)):
  if idades[a]>13 and alturas[a]<soma:
   print(f"Aluno {contador[a]} com {alturas[a]} de altura")