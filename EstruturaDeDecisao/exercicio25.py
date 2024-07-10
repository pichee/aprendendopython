#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
contador=0
variavel=input("Telefonou para a vítima? [S] ou [N]:")
if variavel=='S' or 's':
    contador=contador+1
variavel=input("Esteve no local do crime? [S] ou [N]:")
if variavel=='S' or 's':
    contador=contador+1
variavel=input("Mora perto da vítima?[S] ou [N]:")
if variavel=='S' or 's':
    contador=contador+1
variavel=input("Devia para a vítima? [S] ou [N]:")
if variavel=='S' or 's':
    contador=contador+1
variavel=input("Já trabalhou com a vítima? [S] ou [N]:")
if variavel=='S' or 's':
    contador=contador+1
if contador==2:
    print("Pessoa suspeita")
    ()
if contador==3 or contador==4:
    print("Cúmplice")
    ()
if contador==5:
    print("Assasino")
    exit()
print("Inocente")
