try:
    numero = int(input("Digite um numero:"))
    ver=numero % 2
    if ver == 0:
       print("O numero {} é par".format(numero))
    else:
       print("O numero {} é impar".format(numero))
except:
    print("Voce nao digitou nenhum número")