#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
c=2
resp1=1
resp2=2
resp3=0
aux=0
while resp3<=500:
  resp3=resp1+resp2
  resp1=resp2
  resp2=resp3
  print("{} ".format(resp3))

