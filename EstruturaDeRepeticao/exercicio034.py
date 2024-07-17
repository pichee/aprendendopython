#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
num=int(input("Digite um numero:"))
a=2
while a<num:
    result=num%a
    if result==0:
        print("Esse numero não é primo")
        exit()
    a=a+1

print("Esse numero é primo")
