#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
metros=float(input("Digite a quantidade de metros a serem pintados\n"))
quantidade=metros/6
latao=quantidade/18*80
galao=quantidade/3.6*25
print("\nCaso voce pegue galoes ira pagar {:.2f} e caso pegue latao ira pagar {:.2f}".format(galao,latao))
