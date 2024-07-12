#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
numero=int(input("Digite um numero:"))
print("TABUADA")
i=int(0)
resultado=int(0)
for i in range(11):
    resultado=numero*i
    print("{}X{}={}".format(numero,i,resultado))
