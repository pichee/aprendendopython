#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
#quantos espaços em branco existem na frase.
#quantas vezes aparecem as vogais a, e, i, o, u.
def contadorr(x):
 contador=0
 texto=input("Digite o seu texto:")
 tamanho=len(texto)
 verificar=0
 while verificar<tamanho:
     if texto[verificar]==" ":
         contador=contador+1
     if texto[verificar] == "A" or texto[verificar] == "a" or \
     texto[verificar] == "E" or texto[verificar] == "e" or \
     texto[verificar] == "I" or texto[verificar] == "i" or \
     texto[verificar] == "O" or texto[verificar] == "o" or \
     texto[verificar] == "U" or texto[verificar] == "u":
         contador=contador+1
     verificar=verificar+1

 print(f"Esse texto possui {contador} vogais mais espacos")

contadorr(0)
 