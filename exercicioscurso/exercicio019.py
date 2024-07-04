#Um professor quer sortear um dos seus quatro alunos para apagar o
#quadro. Faça um programa que ajude ele, lendo o nome dos alunos
#escrevendo na tela o nome do escolhido.
import random
n1=input("Enter the first student:")
n2=input("Enter the second student:")
n3=input("Enter the third student:")
n4=input("Enter the Fourth student:")
l=(n1,n2,n3,n4)
r=random.choice(l)
print("The student choose is {}".format(r))
