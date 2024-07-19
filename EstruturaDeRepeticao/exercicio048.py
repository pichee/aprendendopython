#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
#Exemplo:
#  12376489
#  => 98467321
numero = int(input("Digite um número inteiro positivo: "))
numero_invertido = str(numero)[::-1]
numero_invertido = int(numero_invertido)
print(f"O número invertido é: {numero_invertido}")
