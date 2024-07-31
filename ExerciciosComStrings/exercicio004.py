##Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
def nome(x):
  c=0
  nome=input("Digite o nome:")
  tamanho=len(nome)
  for a in range (tamanho):
    c=0
    while c<=a:
     print(f"{nome[c]}",end="")
     c+=1
    print(" ")
nome(0)
