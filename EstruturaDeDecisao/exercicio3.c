#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
sexo=input("Voce é homem[h] ou mulher[f]\n")
if sexo=='H' or sexo=='h':
    print("Voce é homem")

elif sexo=='F' or sexo=='f':
    print("Voce é mulher")
else:
    print("Letra invalida")
