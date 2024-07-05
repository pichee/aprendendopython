#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
ce=float(input("digite a temperatura em celsius:"))
fe=(ce*9/5)+32
print("{:.2f} Celsius equivale a {:.2f} ferenheit".format(ce,fe))