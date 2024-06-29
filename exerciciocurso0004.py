nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
if(nome == "" or idade == ""):
    print("voce nao digitou algum dado")
else:
    print("O seu nome é",nome)
    print("O nome ao contrario é",nome[::-1])
    print("Ele possui 5 letras",len(nome))
    print("A sua Primeira letra é",nome[:1])
    print("A sua Ultima letra é",nome[-1])
    if " " in nome:
        print("Esse nome contem espaço")
    else:
        print("Esse numero não contem espaços")
