def multiplicacao(x):
  soma=1
  numero=0
  while True:
    numero=int(input("Digite um numero:"))
    soma=soma*numero
    decisao=input("voce quer adicionar mais algum numero [s] ou [n]")
    if decisao=="s":
      continue
    else:
      break
  print(f"A multiplicaçao de todos os numeros é {soma}")
multiplicacao(0)