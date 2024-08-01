
#Jogo da palavra embaralhada. Desenvolva um jogo em #que o usuário tenha que adivinhar uma palavra que #será mostrada com as letras embaralhadas. O #programa #terá uma lista de palavras lidas de um #arquivo texto e escolherá uma aleatoriamente. O #jogador terá seis tentativas para adivinhar a #palavra. Ao final a palavra deve ser mostrada na #tela, informando se o usuário ganhou ou perdeu o #jogo.
import random

nomes = ["Doutor-botica", "Banheira", "Glamour-Black", "Alumínio", "Ameixa-negra", "bolacha", "oui"]
sorteio = random.randint(0, 6)
palavrasorteada = nomes[sorteio]
a = 0
tamanhodapalavra = len(palavrasorteada)
palavraembaralhada = [" "] * tamanhodapalavra
posicoes = []

while a < tamanhodapalavra:
    sorteio = random.randint(0, tamanhodapalavra - 1)
    if sorteio not in posicoes:
        posicoes.append(sorteio)
        palavraembaralhada[a] = palavrasorteada[sorteio]
        a += 1

print(f"Palavra embaralhada: {''.join(palavraembaralhada)}")
while True:
    ganhar = input("Digite a palavra que é: ")
    if ganhar == palavrasorteada:
        print("Você ganhou!")
        break 
    else:
        print("Tente novamente.")