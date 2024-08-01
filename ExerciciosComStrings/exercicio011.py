#Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
#Digite uma letra: A
#-> Você errou pela 1ª vez. Tente de novo!
#Digite uma letra: O
#A palavra é: _ _ _ _ O
#Digite uma letra: E
#A palavra é: _ E _ _ O
#Digite uma letra: S
#-> Você errou pela 2ª vez. Tente de novo!
def forca(x):
    import random
    aleatorio=['minecraft','fiorin','computador','coelho','sono']
    palavra=random.randint(0,4)
    ganhar=aleatorio[palavra]
    palavra=aleatorio[palavra]
    tamanho=len(ganhar)
    a=0
    erro=0
    _=["_"]*tamanho
    print(f"{_}")
    while True:
       letra=input("Fale uma letra:")
       a=0
       aux=0
       for a in range(tamanho):
          if letra==palavra[a]:
             _[a]=letra 
             print(f"{_}")
             aux=1
          
        
       if aux==0:
           erro=1+erro
       if "_" not in _:
           print("Voce ganhou")
           exit()
           
       if erro==6:
          print("Voce perdeu")
          exit()




forca(0)