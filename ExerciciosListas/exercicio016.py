#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
saltos=[0,0,0,0,0]
while True:
  nome=input("Informe o nome do atleta:")
  if nome=="":
     exit()
  saltos[0]=float(input("Digite o valor do primeiro salto:"))
  saltos[1]=float(input("Digite o valor do segundo salto:"))
  saltos[2]=float(input("Digite o valor do terceiro salto:"))
  saltos[3]=float(input("Digite o valor do quarto salto:"))
  saltos[4]=float(input("Digite o valor do quinto salto:"))
  media=sum(saltos)
  print(f"Saltitador {nome} valor dos saltos {saltos} media dos saltos {media}\n")