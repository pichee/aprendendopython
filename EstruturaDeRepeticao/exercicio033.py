#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
temp=float(input("Digite a temperatura:"))
maximo=temp
mini=temp
media=temp
contador=2
decisao=input("Voce quer adicionar alguma outra temperatura:\nSim[S] ou Não[n]")
if decisao!='s' and decisao!='S':
    print("A temperatura maxima é {}\nA temperatura minima é {}\n A media das temperaturas é {}".format(maximo,mini,media))
    exit()
else:
    while True:
        temp=float(input("Digite a temperatura:"))
        if temp>maximo:
            maximo=temp
        if temp<mini:
            mini=temp
        media=media+temp

        contador=contador+1
        decisao=input("Voce quer adicionar alguma outra temperatura:\nSim[S] ou Não[n]")
        if decisao!='s' or decisao!='S':
            break

media=media/contador  
print("A temperatura maxima é {}\nA temperatura minima é {}\n A media das temperaturas é {}".format(maximo,mini,media))

