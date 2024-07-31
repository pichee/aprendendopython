#Nome ao contrário em maiúsculas.
 #Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre 
 #o nome do usuário de trás para frente utilizando somente letras maiúsculas.
 # Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
def nomeinvertido(x):
   nome=input("Digite um nome:")
   maisculo=nome.upper()
   maisculo=maisculo[::-1]
   print(f"{maisculo}")
   
nomeinvertido(0)
