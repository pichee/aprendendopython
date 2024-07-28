#Faça um Programa que peça a idade e a altura de 5
#pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
vetoridade=[]
vetoraltura=[]
a=0
for a in range(5):
  altura=float(input(f"Digite a altura da pessoa {a+1}:"))
  idade=int(input(f"Digite a idade da pessoa {a+1}:"))
  vetoridade.append(idade)
  vetoraltura.append(altura)
print(f"as idades são {vetoridade} e as alturas sao {vetoraltura}")
