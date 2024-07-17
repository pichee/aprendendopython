#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turma=int(input("Quantas turmas o colegio tem?"))
alunos=0
media=0
for a  in range(turma):
 alunos=int(input("Quantos alunos a turma{} tem:".format(a+1)))
 if alunos>40:
   print("O numero de alunos nao pode ser maior que 40")
   exit()
 else:
   media=media+alunos
media=media/turma
print("a media de alunos por turma é igual a {:.2f}".format(media))