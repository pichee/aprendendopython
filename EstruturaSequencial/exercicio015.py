#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : 
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
hora=float(input("Quanto voce ganha por hora:"))
trabalho=float(input("Quantas horas voce trabalhou:"))
trabalho=trabalho*hora
inss=0.11*trabalho
ir=0.08*trabalho
sindicato=0.05*trabalho
salario_liquido=trabalho-inss-ir-sindicato
print("Seu salario bruto é {:.2f} com o Ir de {:.2f} mais o inss{:.2f} mais o sindicato de {:.2f} seu salario final é {:.2f}".format(trabalho,ir,sindicato,inss,salario_liquido))


