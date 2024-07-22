vetor=[]
contador=0
a=0
for a in range(2):
  n1=float(input(f"digite a primeira nota do aluno {a+1}:"))
  n2=float(input(f"digite a segunda nota do aluno {a+1}:"))
  n3=float(input(f"digite a terceira nota do aluno {a+1}:"))
  n4=float(input(f"digite a quarta nota do aluno {a+1}:"))
  soma=(n1+n2+n3+n4)/4
  vetor.append(soma)
  if soma>=7:
    contador=contador+1
print(f"O total de alunos que tirou 7 ou mais foi {contador} e essas foram as notas de todos os alunos {vetor} ")