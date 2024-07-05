#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
quadrado=float(input("digite o lado do seu quadrado"))
quadrado=quadrado*quadrado
dobro=quadrado*2
print("O dobro da sua area {:.2f} é igual a {:.2f}".format(quadrado,dobro))