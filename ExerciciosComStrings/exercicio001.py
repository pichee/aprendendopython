#Tamanho de strings. Faça um programa que leia 2 strings e 
#informe o conteúdo delas seguido do seu comprimento.
# Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes
# no conteúdo.
def palavras(frase1,frase2):
  frase1=input("Digite a primeira palavra:")
  frase2=input("Digite a segunda palavra:")
  tamanho1=len(frase1)
  tamanho2=len(frase2)
  if frase1==frase2:
    print(f"Essas frases são iguais e possuem {tamanho1} caracteres")
  else:
    print(f"Essas frases não sao iguais a primeira tem {tamanho1} caracteres e a segunda tem {tamanho2} caracteres")
palavras(0,0)
