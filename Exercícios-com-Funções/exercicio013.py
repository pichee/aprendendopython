#Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
#8  3  4 
#1  5  9
#6  7  2
#Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
def quadrado(x):
    c = 0
    matriz = [0] * 9
    for a in range(9):
        matriz[a] = int(input("Digite um numero:"))

    for a in range(9):
        print(f"{matriz[a]} ", end="")
        c += 1
        if c == 3:
            print("")
            c = 0

    soma1 = sum(matriz[0:3])
    soma2 = sum(matriz[3:6])
    soma3 = sum(matriz[6:9])
    soma_col1 = matriz[0] + matriz[3] + matriz[6]
    soma_col2 = matriz[1] + matriz[4] + matriz[7]
    soma_col3 = matriz[2] + matriz[5] + matriz[8]
    soma_diag1 = matriz[0] + matriz[4] + matriz[8]
    soma_diag2 = matriz[2] + matriz[4] + matriz[6]

    if (
        soma1 == soma2 == soma3 ==
        soma_col1 == soma_col2 == soma_col3 ==
        soma_diag1 == soma_diag2
    ):
        print("É um quadrado mágico!")
    else:
        print("Não é um quadrado mágico.")

quadrado(0)