#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
quantidade=int(input("Digite a a quantidade que deseja sacar[minimo 10 maximo 600]"))
total=quantidade
centena=quantidade//100
quantidade=quantidade%100
cinquenta=quantidade//50
quantidade=quantidade%50
dezena=quantidade//10
quantidade=quantidade%10
cinco=quantidade//5
quantidade=quantidade%5
unidade=quantidade
if total>600:
  print("\nValor maior que o limite")
  exit()
if total<10:
  print("\nValor menor que o limite")
  exit()
print("\nPara sacar a quantia de {} reais,o programa fornecera {} notas de 100,{} notas de 10,{} notas de 5,{} moedas de 1 real".format(total,centena,cinquenta,dezena,cinco,unidade))