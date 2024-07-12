#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
while True:
 nome=input("Digite seu nome:")
 idade=int(input("Digite sua idade:"))
 salario=float(input("Digite seu salario:"))
 sexo=input("voce é masculino[m] ou feminino[f]:")
 estadocivil=input(("Voce está\nSolteiro[s]\nCasado[c]\nDivorciado[d]\nViuvo[v]:"))
 aux=len(nome)
 if aux<3 or idade<0 or idade>150:
  print("Tente novamente")
 elif sexo!='f' and sexo !='m' and estadocivil!='s' and estadocivil!='c' and estadocivil!='v' and estadocivil!='d':
   print("Tente novamente")
 else:
  print("Dados guardados com sucesso")
  exit()