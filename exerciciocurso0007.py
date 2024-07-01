nome =input("Digite seu nome:")
contador=len(nome)
novo =""
contagem=(int(0))
while(contagem<contador):
  novo=novo+nome[contagem]
  contagem+=1
print("{}".format(novo))