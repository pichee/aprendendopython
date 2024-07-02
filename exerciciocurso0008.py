contador=0
escolha=0
total=0
while True:
  try:
     if contador==0:
      numero1=float(input("Digite um numero:"))
      
     numero2=float(input("Digite outro numero:"))
     escolha= int(input("O que voce quer fazer\nSoma[1]\nSubtracão[2]\nDivisão[3]\nMultiplicacão[4]\nPorcetagem"))
     if escolha==1 and contador==0:
      total=numero1+numero2
      print("A soma entre {}+{} é igual a {}".format(numero1,numero2,total))
      
     if escolha==1 and contador > 0:
      auxtotal=total
      total=total+numero2
      print("A soma entre {}+{} é igual a {}".format(auxtotal,numero2,total))
      
      
      
     if escolha==2 and contador==0:
        auxtotal=total
        total=numero1-numero2
        print("A subtração entre {}+{} é igual a {}".format(numero1,numero2,total))
      
      
     if escolha==2 and contador>0 :
         auxtotal=total
         total=total-numero2
         print("A soma entre {}+{} é igual a {}".format(auxtotal,numero2,total))
      
      
     if escolha==3 and contador==0:
         auxtotal=total
         total=numero1/numero2
         print("A divisão entre {}+{} é igual a {}".format(numero1,numero2,total))
      
       
      
     if escolha==3 and contador>0:
         auxtotal=total
         total=total/numero2
         print("A divisão entre {}+{} é igual a {}".format(auxtotal,numero2,total))
      
      
      
     if escolha==4 and contador==0:
       total=numero1*numero2
       print("A multiplicação entre {}+{} é igual a {}".format(numero1,numero2,total))
      
      
     if escolha==4 and contador>0:
      auxtotal=total
      total=total*numero2
      print("A divisão entre {}+{} é igual a {}".format(auxtotal,numero2,total))
      
     escolhanumero=input("Voce quer alguma operação com o resultado {}?[S ou N]".format(total))
     if escolhanumero=="S" or escolhanumero=="s":
      contador=1
     else:
         contador=0
     
      
  except:
    print("algo deu errado tente novamente\n")
    contador=0