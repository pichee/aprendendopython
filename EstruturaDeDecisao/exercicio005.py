#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1=float(input("Qual foi a primeira nota"))
nota2=float(input("Qual foi a segunda nota"))
nota1=(nota1+nota2)/2
if nota1<7:
  print("Reprovado")
elif nota1==10:
  print("Aprovado com Distinção")
elif nota1>10:
  print("Erro")
else:
  print("Aprovado")