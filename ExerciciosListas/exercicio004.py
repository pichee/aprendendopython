#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
vetoro=input("Digite um nome:")[:9]
a=0
cont=0
print(f"A palavra {vetoro} tem:")
for a in range(len(vetoro)):
  if (vetoro[a]!='a' and vetoro[a]!='A' and vetoro[a]!='e' and vetoro[a]!='E' and vetoro[a]!='i' and vetoro[a]!='I' and vetoro[a]!='o' and vetoro[a]!='O' and vetoro[a]!='u' and vetoro[a]!='U'):
    print(f"{vetoro[a]}")
    cont=cont+1
print(f"Totalizando {cont} vogais")