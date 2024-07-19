##Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
# valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
##Os juros e a quantidade de parcelas seguem a tabela abaixo:
#Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
#1       0
#3       10
#6       15
#9       20
#12      25
#Exemplo de saída do programa:
#Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
#R$ 1.000,00     0               1                       R$  1.000,00
#R$ 1.100,00     100             3                       R$    366,00
#R$ 1.150,00     150             6                       R$    191,67
divida=float(input("Qual o valor da divida:"))
parcela=int(input("Qual a quantidade de parcelas:"))
total=0
if parcela<1:
  total=divida
  juros=0
elif parcela<=3:
  total=divida*0.1+divida
  juros=10
elif parcela<=6:
  total=divida*0.15+divida
  juros=15
elif parcela<=9:
  total=divida*0.20+divida
  juros=20
elif parcela>=12:
  total=divida*0.25+divida
  juros=25

soma=total/juros
print("Valor da divida:{}\nValor do juros:{}%\nQuantidade de parcelas:{}\nvalor total:{}\nvalor da parcela:{}".format(divida,juros,parcela,total,soma))