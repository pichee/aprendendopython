#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
def nome(x):
  nome=input("Digite o nome:")
  tamanho=int(len(nome))
  aux=0
  for a in range (tamanho):
    c=tamanho-1
    aux=0
    while c>=a:
     print(f"{nome[aux]}",end="")
     c=c-1
     aux=aux+1
    print(" ")
nome(0)