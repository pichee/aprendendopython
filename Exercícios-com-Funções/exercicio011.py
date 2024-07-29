#Data com mês por extenso. 
#Construa uma função que receba uma data no formato 
#DD/MM/AAAA e devolva uma string no formato
# D de mesPorExtenso de AAAA. Opcionalmente,
# valide a data e retorne NULL caso a data
# seja inválida.
def data():
  dia=int(input("Informe o dia:"))
  mes=int(input("Informe o mes:"))
  ano=int(input("Informe o ano:"))
  
  if dia>31 or dia<0:
    print("Data invalida")
    exit()
  elif mes>12 or mes<0:
    print("Data invalida")
    exit()
  elif ano<0:
    print("Data invalida")
    exit()
  if mes == 1:
    estenco_mes = "janeiro"
  elif mes == 2:
    estenco_mes = "fevereiro"
  elif mes == 3:
    estenco_mes = "março"
  elif mes == 4:
    estenco_mes = "abril"
  elif mes == 5:
    estenco_mes = "maio"
  elif mes == 6:
    estenco_mes = "junho"
  elif mes == 7:
    estenco_mes = "julho"
  elif mes == 8:
    estenco_mes = "agosto"
  elif mes == 9:
    estenco_mes = "setembro"
  elif mes == 10:
    estenco_mes = "outubro"
  elif mes == 11:
    estenco_mes = "novembro"
  else:
    estenco_mes = "dezembro"
  print(f"A Data ê {dia} de {estenco_mes} de {ano}")
  
data()
    