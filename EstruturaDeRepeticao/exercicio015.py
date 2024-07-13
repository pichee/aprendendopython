#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
livre=int(input("Qual numero voce quer?"))
if livre==1 or livre==2:
  print("1")
c=2
resp1=1
resp2=2
resp3=0
contador=2
aux=0
while contador!=livre:
  resp3=resp1+resp2
  resp1=resp2
  resp2=resp3
  contador=contador+1
  
print("{}".format(resp3))
  
  