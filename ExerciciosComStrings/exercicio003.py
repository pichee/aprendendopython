##Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
def nome(x):
  nome=input("Digite o nome:")
  tamanho=len(nome)
  for a in range (tamanho):
    print(f"{nome[a]}")
  
nome(0)
