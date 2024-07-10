#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
numero=float(input("Digite um numero"))
teste=round(numero)
if teste==numero:
  print("Esse numero é do tipo inteiro")
else:
  print("Esse numero é do tipo decimal")