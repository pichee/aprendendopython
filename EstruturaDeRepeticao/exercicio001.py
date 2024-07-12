#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
while True:
  numero=int(input("digite um  numumero de 1 a 10:"))
  if numero>=1 and numero<=10:
    break
  else:
    print("numero invalido tente novamente\n")