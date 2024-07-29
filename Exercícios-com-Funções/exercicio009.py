#Reverso do número. 
#Faça uma função que retorne o
# reverso de um número 
#inteiro informado. 
#Por exemplo: 127 -> 721.
def reverso(x):
  numero=int(input("Digite um numero:"))
  inversao=str(numero)[::-1]
  print(f"{inversao}")
reverso(0)