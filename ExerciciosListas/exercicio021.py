#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#O modelo do carro mais econômico;
#Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. 
#Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
carros=[]
kms=[]
economico=999
a=0
for a in range(4):
  carro=input("Nome do carro:")
  km=float(input("Quantidade feita por litro"))
  carros.append(carro)
  kms.append(km)
  if economico>km:
    economico=km
a=0
for a in range(4):
  print(f"Nome do carro {a+1}:{carros[a]}\nQuantidade por litro:{kms[a]}")
print(f"Carro mais economico faz por litro {economico}")