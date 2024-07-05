#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
fa=float(input("qual a temperatura em graus Fahrenheit"))
c= 5 * ((fa-32) / 9)
print("A temperatura {:.2f} em celsius é {:.2f}".format(fa,c))