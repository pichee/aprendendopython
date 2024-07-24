#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
cont=[0]
print("Questionario:\n")
questao=input("Telefonou para a vítima [s] ou [n]:")
if questao=="s":
  cont[0]=cont[0]+1
questao=input("Esteve no local do crime  [s] ou [n]:")
if questao=="s":
  cont[0]=cont[0]+1
questao=input("Mora perto da vítima [s] ou [n]:")
if questao=="s":
  cont[0]=cont[0]+1
questao=input("Devia para a vitima [s] ou [n]:")
if questao=="s":
  cont[0]=cont[0]+1
questao=input("Já trabalhou com a vítima [s] ou [n]:")
if questao=="s":
  cont[0]=cont[0]+1
if cont[0]==2:
    print("SUSPEITA")
elif cont[0]==3 or cont[0]==4:
    print("CÚMPLICE")
elif cont[0]==5:
    print("Assassino")
else:
    print("Inocente ")