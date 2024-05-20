# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele

#Make a program read something the keyboard
#Show in the scream your type
#and other informations

m = input('Enter something: ')
print("Type {}".format(type(m)))
print('Something is numeric:', m.isnumeric())
print('Something is alphanumeric:', m.isalnum())
print('The something has just letters:', m.isalpha())
print('All characters in something are in ASCII:', m.isascii())
print('The something is a decimal string:', m.isdecimal())
print('The something is a digit:', m.isdigit())
print('The something is a valid Python identifier:', m.isidentifier())
print('The something is a space:', m.isspace())
print('The something is printable:', m.isprintable())
print('The something is in lowercase:', m.islower())
print('The something is in uppercase:', m.isupper())
print('The something is title-cased:', m.istitle())
