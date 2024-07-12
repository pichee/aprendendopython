#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
c=int(0)
a=int(80000)
b=int(200000)
while True:
  a=a+(a*0.03)
  b=b+(b*0.015)
  c=c+1
  if a>=b:
    print("vai levar {} anos para A passar ou se igualar a B".format(c))
    exit()
  