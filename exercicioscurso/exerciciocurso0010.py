lista=[]
add=0
contador=0
while True:
    decisao=input("O que voce quer fazer\nSair[s] Apagar[a] Inserir[i]:\n")
    if decisao=='i':
        add=input("Digite O item:")
        lista.append(add)
    if decisao=='a':
        add=int(input("Digite O item a apagar:"))
        contador=len(lista)
        add=add-1
        if add>contador:
                print("O Item não foi encontrado tente novamente")
        else:
                 lista.pop(add)
    if decisao=='s':
        print(f"Lista final:{lista}")
        exit()
    print(f"Lista:\n{lista}")
    
