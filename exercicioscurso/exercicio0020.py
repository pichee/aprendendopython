#O mesmo professor do desafio 019 quer sortear a ordem de 
#trabalhos dos alunos. Faça um programa que leia o nome dos quatro
#alunos e mostre a ordem sorteada.
import random
n1=input("Enter the first student:")
n2=input("Enter the second student:")
n3=input("Enter the third student:")
n4=input("Enter the Fourth student:")
l=[n1,n2,n3,n4]
random.shuffle(l)
print("The student choose is {}".format(l))
