#Jogo de Craps.
# Faça um programa de implemente um jogo de Craps. 
# O jogador lança um par de dados, obtendo um valor 
#entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, 
#você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto,
# se tirar um 7 antes de tirar este Ponto novamente.
import random
def craps(x):
  import random
  aux=0
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  soma=dado1+dado2
  if soma==2 or soma==3 or soma==12:
    
    print(f"Voce perdeu pois tirou {soma}")
    exit()
  if soma==7 or soma==11:
    print(f"Voce ganhou pois tirou {soma}")
  else:
    print(f"Voce ganhou um ponto pois tirou {soma} tire esse numero denovo")
    while True:
      if soma!=aux:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        aux=dado1+dado2
      else:
        break
      if aux==7:
        print("Voce perdeu")
        exit()
  print("Parabens voce ganhou")
craps(0)