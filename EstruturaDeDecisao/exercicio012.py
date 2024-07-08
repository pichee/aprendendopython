##Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
##Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
horas=float(input("Quantas horas voce trabalhou"))
ganhar=float(input("Quanto voce receber por hora:"))
salario=horas*ganhar
if salario<=900:
  print("Seu salario descontado os impostos fica {:.2f}".format(salario))
elif salario>900 and salario <=1500:
  salario=salario-(salario*0.05)
  print("Seu salario descontado os impostos fica {:.2f}".format(salario))
elif salario>1500 and salario <=2500:
  salario=salario-(salario*0.10)
  print("Seu salario descontado os impostos fica {:.2f}".format(salario))
else:
  salario=salario-(salario*0.20)
  print("Seu salario descontado os impostos fica {:.2f}".format(salario))
   
    