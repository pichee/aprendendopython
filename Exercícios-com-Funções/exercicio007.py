#Faça um programa que use a função valor
#Pagamento para determinar o valor a ser pago por uma prestação de uma conta. 
#O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
# estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
#O programa deverá então exibir o valor a ser pago na tela. 
#Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual 
#a zero para a prestação. Neste momento o programa deverá ser encerrado, 
#exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
#Faça uma função que informe a
def pagamento(x):
  quantidade_prestacao=0
  valortotal=0
  while True:
    prestacao=float(input("Digite quanto custa a prestação:"))
    dias_atraso=int(input("Digite a quantidade de dias em atraso:"))
    if prestacao==0:
      break
    quantidade_prestacao=1+quantidade_prestacao
    pagamentofinal=(prestacao*0.03)+prestacao
    _=1
    while _<=dias_atraso:
      pagamentofinal=pagamentofinal*0.01+pagamentofinal
      _+=1
    valortotal+=pagamentofinal
    encerramento=input("Deseja encerrar o programa Sim[s] ou Não[n]:")
    if encerramento=="s":
     break
  print(f"O total de prestações foi igual a {quantidade_prestacao:.2f} e o valor arrecadado é igual a {valortotal}")
pagamento(0)