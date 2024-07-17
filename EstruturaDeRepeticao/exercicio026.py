#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
povo=int(input("Quantas pessoas vao votar:"))
c1=0
c2=0
c3=0
nulo=0
for a in range(povo):
  voto=int(input("A {}° pessoa vai votar no \ncandidato 1 [1]\ncantidato 2 [2]\ncandidato 3[3]\nvoto:".format(a+1)))
  if voto==1:
     c1=c1+1
  elif voto==2:
     c2=c2+1
  elif voto==3:
    c3=c3+1
  else:
    nulo=nulo+1

print("Os resultados foram:\n {} votos para o canditado 1\n{} votos para o canditado 2\n{} votos para o canditado 3\n {} nulos".format(c1,c2,c3,nulo))
    
    