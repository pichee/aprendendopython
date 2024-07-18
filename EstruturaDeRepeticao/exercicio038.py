#Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
salario=float(input("Digite o salario do cidadão de 1995:"))
percent=0.15
for c in range(29):
  salario=(salario*percent)+salario
print("O salario dessa pessoa em 2024 sera {:.2f}".format(salario))