#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
vetor=[]
for a in range(4):
    numero=float(input("Digite a nota:"))
    vetor.append(numero)
soma=sum(vetor)
soma=soma/4
print(f"A Media da turma é {soma}")
