#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
#Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def funcao(x):
    while True:
        hora=int(input("digite apenas a hora:"))
        if hora>24 or hora<0:
            print("Hora incorreta tente novamente\n")
            continue
        minutos=int(input("Digite os minutos:"))
        if minutos>60 or minutos<0:
            print("Minutos  incorretos tente novamente\n")
        else:
            break
        
    if hora<=12:
        print(f"{hora}:{minutos}AM")
    else:
        hora=hora-12
        print(f"{hora}:{minutos}PM")
             

while True:
    funcao(0)
    escolha=input("Quer adicionar mais alguma hora:Sim[s] ou Não[n]:")
    if escolha=='n':
        exit()
