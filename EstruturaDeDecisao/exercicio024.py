#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
num1=float(input("Qual o primeiro numero:"))
num2=float(input("Qual o segundo numero:"))
pergunta=int(input("O que voce quer fazer:\nadição[1]\nsubtração[2]\nmultiplicação[3]\ndivisão[4]\n"))
if pergunta==1:
  resp=num1+num2
  print("{}+{}={}".format(num1,num2,resp))
  if numero>=0:
    print("Numero positivo")
  else:
    print("Numero negativo")
  teste=resp
  if teste==round(resposta):
    print("Esse numero nao é um numero flutuante")
  else:
    print("Esse numero é um numero flutuante")

if pergunta==2:
  resp=num1-num2
  print("{}-{}={}".format(num1,num2,resp))
  if resp>=0:
    print("Numero positivo")
  else:
    print("Numero negativo")
   
  teste=resp
  if teste==round(resp):
    print("Esse numero nao é um numero flutuante")
  else:
    print("Esse numero é um numero flutuante")
if pergunta==3:
  resp=num1*num2
  print("{}*{}={}".format(num1,num2,resp))
  if resp>=0:
    print("Numero positivo")
  else:
    print("Numero negativo")
   
  teste=resp
  if teste==round(resp):
    print("Esse numero nao é um numero flutuante")
  else:
    print("Esse numero é um numero flutuante")

if pergunta==4:
  resp=num1*num2
  print("{}*{}={}".format(num1,num2,resp))
  if resp>=0:
    print("Numero positivo")
  else:
    print("Numero negativo")
   
  teste=resp
  if teste==round(resp):
    print("Esse numero nao é um numero flutuante")
  else:
    print("Esse numero é um numero flutuante")
if pergunta>4:
  print("ERROR")
    
