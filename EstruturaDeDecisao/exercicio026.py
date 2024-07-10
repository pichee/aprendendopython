#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros=int(input("Quanots litros voce comprou:"))
combustivel=input("Adquiriu o Alcool[A] ou Gasolina[G]:")
if combustivel !='A' and combustivel!='G':
    print("Combustivel invalido")
    exit()
if combustivel=='A':
    alcol=1.9
    alcol=1.9*litros
    if litros>20:
        venda=alcol-(alcol*0.05)
    else:
        venda=alcol-(alcol*0.03)
if combustivel=='G':
    gasolina=2.5
    alcol=2.5*litros
    if litros>20:
        venda=gasolina-(gasolina*0.06)
    else:
        venda=gasolina-(gasolina*0.03)

print("O total a ser pago é igual a {}".format(venda))
